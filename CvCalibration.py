import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob
import os

def calibrate_with_multiple_images(image_paths, chessboard_size, square_size_mm):
    n_rows, n_cols = chessboard_size

    # Satranç tahtası köşeleri için 3D dünya koordinatlarını tanımla
    objp = np.zeros((n_rows * n_cols, 3), np.float32)
    objp[:, :2] = np.mgrid[0:n_cols, 0:n_rows].T.reshape(-1, 2) * (square_size_mm / 10)  # mm'yi cm'ye çevir

    objpoints = []  # 3D dünya noktaları
    imgpoints = []  # 2D görüntü noktaları

    for idx, image_path in enumerate(image_paths):
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Satranç tahtası köşelerini bul
        ret, corners = cv2.findChessboardCorners(gray, (n_cols, n_rows), None)

        if ret:
            objpoints.append(objp)
            corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1),
                                        criteria=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001))
            imgpoints.append(corners2)

            # Köşeleri çiz ve göster
            cv2.drawChessboardCorners(img, (n_cols, n_rows), corners2, ret)
            cv2.imshow(f'Satranç Tahtası Köşeleri - {os.path.basename(image_path)}', img)
            cv2.waitKey(300)  # Her resmi 300ms gösterir
        else:
            print(f"Satranç tahtası köşeleri bulunamadı: {image_path}")

    cv2.destroyAllWindows()

    # Kamera kalibrasyonu
    ret, cam_matrix, dist_coeffs, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
    return cam_matrix, dist_coeffs, rvecs, tvecs

def remove_distortion(image_path, cam_matrix, dist_coeffs):
    img = cv2.imread(image_path)
    h, w = img.shape[:2]
    new_cam_matrix, roi = cv2.getOptimalNewCameraMatrix(cam_matrix, dist_coeffs, (w, h), 1, (w, h))

    undistorted_img = cv2.undistort(img, cam_matrix, dist_coeffs, None, new_cam_matrix)
    
    # Orijinal ve düzeltilmiş görüntüleri göster
    plt.subplot(1, 2, 1)
    plt.title("Orijinal Görüntü")
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.subplot(1, 2, 2)
    plt.title("Düzeltilmiş Görüntü")
    plt.imshow(cv2.cvtColor(undistorted_img, cv2.COLOR_BGR2RGB))
    plt.show()

# Ana fonksiyon
if _name_ == "_main_":
    # Satranç tahtası ayarları
    chessboard_size = (6, 8)  # 6 satır, 8 sütun (iç köşeler)
    square_size_mm = 40  # mm cinsinden kare boyutu

    # Görüntü yollarını '/home/test/Desktop/calibration/images' klasöründen al
    image_folder = "/home/test/Desktop/calibration/images"
    image_paths = glob.glob(os.path.join(image_folder, "*.jpg"))  # .jpg dosyalarını al

    # Kamera kalibrasyonu
    cam_matrix, dist_coeffs, rvecs, tvecs = calibrate_with_multiple_images(image_paths, chessboard_size, square_size_mm)
    
    if cam_matrix is not None and dist_coeffs is not None:
        print("Kamera Matrisi:\n", cam_matrix)
        print("Distorsiyon Katsayıları:\n", dist_coeffs)
        print("Rotation Vektörleri:\n", rvecs)
        print("Translation Vektörleri:\n", tvecs)

        # Distorsiyonu kaldırmak için clearimxi görüntüsünü kullan
        remove_distortion("/home/test/Desktop/calibration/clearimx.jpg", cam_matrix, dist_coeffs)