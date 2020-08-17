#!/usr/bin/python3
from random import shuffle
from base64 import b64encode

printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

datalist = [137, 80, 78, 71, 13, 10, 26, 10, 0, 0, 0, 13, 73, 72, 68, 82, 0, 0, 1, 244, 0, 0, 0, 100, 8, 6, 0, 0, 0, 112, 199, 194, 125, 0, 0, 1, 133, 105, 67, 67, 80, 73, 67, 67, 32, 112, 114, 111, 102, 105, 108, 101, 0, 0, 40, 145, 125, 145, 61, 72, 195, 64, 28, 197, 95, 83, 165, 34, 45, 14, 22, 17, 17, 205, 80, 157, 44, 136, 138, 56, 74, 21, 139, 96, 161, 180, 21, 90, 117, 48, 185, 244, 67, 104, 210, 144, 164, 184, 56, 10, 174, 5, 7, 63, 22, 171, 14, 46, 206, 186, 58, 184, 10, 130, 224, 7, 136, 147, 163, 147, 162, 139, 148, 248, 191, 164, 208, 34, 198, 131, 227, 126, 188, 187, 247, 184, 123, 7, 8, 245, 50, 83, 205, 142, 113, 64, 213, 44, 35, 21, 143, 137, 217, 220, 138, 24, 120, 69, 0, 67, 8, 161, 15, 195, 18, 51, 245, 68, 122, 33, 3, 207, 241, 117, 15, 31, 95, 239, 162, 60, 203, 251, 220, 159, 35, 164, 228, 77, 6, 248, 68, 226, 89, 166, 27, 22, 241, 58, 241, 244, 166, 165, 115, 222, 39, 14, 179, 146, 164, 16, 159, 19, 143, 25, 116, 65, 226, 71, 174, 203, 46, 191, 113, 46, 58, 44, 240, 204, 176, 145, 73, 205, 17, 135, 137, 197, 98, 27, 203, 109, 204, 74, 134, 74, 60, 69, 28, 81, 84, 141, 242, 133, 172, 203, 10, 231, 45, 206, 106, 185, 202, 154, 247, 228, 47, 12, 230, 181, 229, 52, 215, 105, 14, 34, 142, 69, 36, 144, 132, 8, 25, 85, 108, 160, 12, 11, 81, 90, 53, 82, 76, 164, 104, 63, 230, 225, 31, 112, 252, 73, 114, 201, 228, 218, 0, 35, 199, 60, 42, 80, 33, 57, 126, 240, 63, 248, 221, 173, 89, 152, 156, 112, 147, 130, 49, 160, 243, 197, 182, 63, 70, 128, 192, 46, 208, 168, 217, 246, 247, 177, 109, 55, 78, 0, 255, 51, 112, 165, 181, 252, 149, 58, 48, 243, 73, 122, 173, 165, 69, 142, 128, 158, 109, 224, 226, 186, 165, 201, 123, 192, 229, 14, 208, 255, 164, 75, 134, 228, 72, 126, 154, 66, 161, 0, 188, 159, 209, 55, 229, 128, 222, 91, 160, 123, 213, 237, 173, 185, 143, 211, 7, 32, 67, 93, 45, 221, 0, 7, 135, 192, 104, 145, 178, 215, 60, 222, 221, 213, 222, 219, 191, 103, 154, 253, 253, 0, 139, 199, 114, 177, 166, 1, 252, 132, 0, 0, 0, 6, 98, 75, 71, 68, 0, 0, 0, 0, 0, 0, 249, 67, 187, 127, 0, 0, 0, 9, 112, 72, 89, 115, 0, 0, 46, 35, 0, 0, 46, 35, 1, 120, 165, 63, 118, 0, 0, 0, 7, 116, 73, 77, 69, 7, 228, 7, 30, 13, 26, 12, 242, 164, 42, 43, 0, 0, 0, 25, 116, 69, 88, 116, 67, 111, 109, 109, 101, 110, 116, 0, 67, 114, 101, 97, 116, 101, 100, 32, 119, 105, 116, 104, 32, 71, 73, 77, 80, 87, 129, 14, 23, 0, 0, 27, 60, 73, 68, 65, 84, 120, 218, 237, 157, 121, 160, 28, 85, 149, 198, 191, 187, 84, 85, 119, 67, 144, 16, 242, 84, 22, 145, 8, 65, 2, 132, 101, 68, 194, 200, 154, 1, 194, 34, 75, 8, 19, 117, 100, 68, 17, 112, 65, 1, 137, 128, 44, 162, 163, 140, 108, 6, 70, 64, 113, 68, 16, 69, 25, 198, 40, 129, 4, 132, 128, 19, 2, 24, 134, 200, 162, 16, 8, 16, 8, 35, 2, 34, 1, 141, 108, 175, 187, 170, 238, 50, 127, 84, 191, 170, 110, 222, 158, 215, 239, 189, 126, 241, 251, 253, 153, 188, 174, 174, 190, 117, 207, 249, 206, 57, 247, 222, 83, 2, 128, 7, 33, 132, 16, 66, 198, 52, 146, 67, 64, 8, 33, 132, 80, 208, 9, 33, 132, 16, 66, 65, 39, 132, 16, 66, 8, 5, 157, 16, 66, 8, 33, 20, 116, 66, 8, 33, 132, 130, 78, 8, 33, 132, 16, 10, 58, 33, 132, 16, 66, 40, 232, 132, 16, 66, 8, 161, 160, 19, 66, 8, 33, 20, 116, 66, 8, 33, 132, 80, 208, 9, 33, 132, 16, 66, 65, 39, 132, 16, 66, 8, 5, 157, 16, 66, 8, 161, 160, 19, 66, 8, 33, 132, 130, 78, 8, 33, 132, 16, 10, 58, 33, 132, 16, 66, 40, 232, 132, 16, 66, 8, 5, 157, 16, 66, 8, 33, 20, 116, 66, 8, 33, 132, 80, 208, 9, 33, 132, 16, 66, 65, 39, 132, 16, 66, 40, 232, 132, 16, 66, 8, 161, 160, 19, 66, 8, 33, 132, 130, 78, 8, 33, 132, 16, 10, 58, 33, 132, 16, 66, 65, 39, 132, 16, 66, 8, 5, 157, 16, 66, 8, 33, 20, 116, 66, 8, 33, 132, 180, 175, 160, 151, 158, 47, 161, 226, 43, 168, 184, 74, 251, 13, 198, 28, 153, 221, 155, 175, 32, 188, 63, 228, 236, 88, 75, 196, 44, 129, 96, 73, 128, 210, 234, 18, 42, 73, 37, 31, 83, 117, 133, 106, 249, 119, 169, 185, 42, 191, 126, 240, 235, 128, 131, 223, 102, 168, 43, 26, 158, 207, 175, 248, 124, 200, 216, 177, 249, 198, 239, 169, 36, 21, 148, 94, 41, 33, 184, 39, 128, 248, 168, 104, 219, 177, 209, 156, 30, 35, 36, 114, 135, 8, 168, 79, 40, 168, 237, 21, 196, 187, 4, 68, 69, 64, 132, 2, 62, 245, 240, 111, 122, 248, 63, 123, 216, 39, 45, 236, 45, 22, 254, 90, 159, 127, 174, 226, 91, 19, 248, 164, 119, 164, 72, 103, 164, 16, 51, 4, 202, 183, 151, 7, 253, 121, 255, 55, 143, 234, 248, 106, 255, 65, 209, 55, 37, 162, 57, 17, 68, 185, 13, 39, 253, 174, 128, 62, 75, 67, 237, 172, 32, 55, 150, 16, 37, 1, 31, 123, 248, 53, 30, 246, 247, 22, 230, 18, 3, 191, 216, 143, 238, 60, 105, 120, 62, 238, 85, 135, 218, 196, 26, 141, 103, 56, 18, 139, 231, 74, 144, 239, 89, 187, 124, 166, 118, 102, 13, 238, 2, 55, 252, 194, 117, 177, 130, 62, 80, 67, 190, 71, 66, 172, 39, 0, 7, 184, 53, 14, 246, 113, 11, 115, 185, 129, 159, 239, 199, 214, 160, 111, 6, 168, 47, 42, 200, 93, 37, 228, 22, 50, 179, 193, 178, 0, 20, 224, 147, 186, 29, 62, 99, 97, 127, 97, 225, 46, 115, 237, 117, 239, 1, 32, 55, 150, 144, 123, 74, 232, 93, 53, 226, 157, 98, 184, 175, 184, 182, 27, 98, 10, 250, 8, 136, 72, 112, 113, 128, 224, 31, 3, 160, 135, 96, 82, 68, 2, 34, 18, 192, 4, 64, 109, 167, 128, 89, 128, 61, 215, 194, 44, 52, 176, 39, 219, 177, 21, 180, 204, 16, 185, 152, 251, 196, 35, 189, 37, 133, 189, 201, 194, 223, 229, 129, 23, 70, 191, 250, 18, 157, 29, 65, 140, 111, 14, 52, 68, 37, 11, 174, 228, 166, 18, 122, 47, 141, 248, 210, 24, 238, 107, 142, 243, 150, 140, 30, 29, 64, 120, 123, 8, 189, 243, 219, 220, 179, 2, 100, 135, 132, 236, 144, 208, 211, 52, 226, 139, 98, 184, 175, 143, 157, 185, 90, 122, 164, 4, 185, 81, 207, 65, 148, 40, 9, 136, 119, 11, 200, 119, 75, 4, 123, 4, 72, 103, 166, 72, 15, 75, 129, 55, 70, 239, 126, 237, 28, 139, 206, 57, 157, 64, 7, 32, 246, 19, 80, 71, 40, 4, 135, 5, 16, 37, 129, 232, 148, 8, 181, 101, 181, 182, 11, 170, 184, 134, 62, 156, 2, 119, 140, 64, 105, 97, 9, 193, 222, 61, 139, 121, 175, 145, 249, 150, 10, 193, 81, 99, 175, 60, 169, 78, 84, 121, 102, 158, 252, 44, 129, 153, 101, 224, 175, 27, 125, 49, 23, 179, 5, 162, 175, 119, 23, 243, 110, 127, 55, 78, 32, 58, 45, 130, 248, 172, 224, 228, 37, 163, 151, 12, 222, 16, 228, 98, 238, 86, 59, 212, 46, 168, 161, 115, 143, 78, 84, 63, 87, 133, 121, 200, 100, 115, 181, 44, 16, 125, 57, 130, 216, 103, 236, 204, 213, 1, 87, 237, 4, 16, 236, 19, 32, 184, 177, 77, 124, 224, 106, 192, 95, 239, 97, 102, 27, 36, 215, 36, 121, 34, 166, 63, 215, 126, 249, 48, 51, 244, 225, 98, 79, 32, 154, 27, 65, 78, 40, 98, 38, 247, 170, 131, 185, 219, 192, 45, 117, 240, 143, 120, 248, 23, 60, 196, 118, 2, 226, 253, 2, 114, 170, 132, 154, 170, 160, 38, 171, 166, 167, 210, 41, 58, 123, 143, 198, 190, 42, 81, 250, 70, 41, 139, 38, 159, 178, 136, 223, 31, 15, 234, 22, 91, 93, 210, 85, 91, 215, 215, 200, 13, 96, 207, 107, 159, 234, 66, 112, 90, 0, 177, 126, 221, 153, 164, 64, 114, 123, 2, 123, 163, 133, 255, 173, 135, 152, 42, 160, 102, 42, 4, 135, 6, 16, 101, 1, 81, 22, 8, 79, 10, 17, 127, 63, 230, 28, 94, 135, 169, 109, 49, 184, 121, 31, 62, 20, 66, 239, 50, 2, 238, 242, 67, 64, 176, 103, 38, 100, 190, 230, 17, 127, 62, 134, 255, 101, 150, 5, 250, 165, 30, 201, 247, 19, 136, 103, 5, 212, 150, 10, 98, 61, 1, 249, 9, 9, 187, 100, 108, 84, 242, 124, 213, 195, 253, 209, 193, 62, 105, 225, 30, 117, 240, 143, 121, 248, 103, 178, 223, 38, 118, 22, 80, 51, 20, 130, 253, 130, 60, 240, 14, 246, 9, 96, 246, 55, 240, 119, 182, 79, 22, 108, 207, 176, 240, 199, 122, 136, 72, 64, 190, 175, 253, 242, 97, 10, 250, 48, 17, 94, 30, 22, 98, 238, 129, 116, 81, 138, 116, 118, 247, 18, 146, 95, 233, 225, 225, 225, 224, 96, 96, 128, 61, 129, 224, 204, 0, 114, 171, 177, 87, 60, 233, 18, 77, 255, 166, 7, 158, 109, 147, 123, 58, 68, 20, 142, 216, 3, 181, 185, 53, 184, 51, 139, 50, 165, 95, 225, 97, 110, 48, 112, 167, 58, 148, 46, 44, 1, 26, 80, 219, 42, 136, 19, 4, 252, 15, 60, 39, 50, 129, 60, 85, 230, 25, 179, 127, 221, 195, 221, 49, 124, 101, 110, 57, 67, 230, 94, 217, 61, 231, 114, 49, 111, 10, 196, 31, 119, 80, 91, 102, 193, 179, 216, 104, 236, 100, 232, 181, 9, 189, 7, 81, 254, 97, 15, 115, 181, 129, 61, 212, 162, 244, 223, 165, 44, 155, 215, 128, 60, 88, 194, 222, 217, 70, 1, 203, 27, 217, 28, 16, 19, 69, 145, 36, 180, 211, 92, 109, 185, 3, 253, 164, 64, 240, 155, 0, 165, 87, 75, 168, 164, 21, 84, 210, 10, 202, 127, 45, 35, 124, 40, 132, 252, 214, 0, 190, 110, 92, 182, 51, 54, 184, 59, 64, 244, 108, 132, 242, 107, 229, 236, 58, 174, 130, 114, 92, 70, 233, 149, 18, 194, 71, 66, 168, 203, 250, 222, 49, 221, 227, 238, 218, 105, 64, 112, 75, 128, 210, 75, 245, 221, 215, 182, 130, 210, 234, 210, 224, 127, 227, 44, 129, 242, 95, 203, 197, 245, 23, 55, 151, 134, 228, 23, 37, 244, 212, 34, 86, 74, 110, 73, 144, 30, 52, 192, 245, 160, 123, 129, 244, 224, 20, 241, 228, 49, 152, 33, 118, 197, 47, 110, 240, 66, 40, 207, 145, 8, 151, 133, 40, 189, 82, 66, 57, 46, 163, 98, 43, 40, 119, 150, 81, 250, 83, 9, 225, 178, 16, 234, 187, 10, 152, 188, 22, 85, 131, 143, 168, 252, 190, 236, 83, 182, 73, 204, 155, 156, 228, 37, 14, 230, 119, 166, 248, 220, 33, 170, 91, 134, 150, 239, 214, 191, 168, 151, 185, 215, 1, 148, 223, 202, 230, 69, 244, 88, 212, 123, 176, 119, 127, 113, 45, 121, 106, 11, 76, 112, 51, 160, 252, 70, 125, 62, 218, 202, 128, 118, 225, 202, 111, 21, 39, 58, 162, 229, 209, 200, 78, 147, 57, 18, 225, 253, 97, 102, 67, 105, 5, 229, 106, 25, 165, 63, 150, 160, 175, 215, 192, 184, 62, 178, 143, 121, 186, 120, 6, 63, 234, 219, 254, 131, 69, 65, 241, 183, 223, 25, 218, 233, 138, 224, 243, 1, 208, 85, 224, 89, 144, 2, 15, 15, 167, 234, 13, 192, 59, 55, 60, 46, 255, 202, 192, 108, 173, 149, 99, 55, 156, 190, 213, 47, 244, 112, 171, 26, 108, 116, 253, 54, 180, 3, 59, 92, 234, 217, 102, 25, 186, 190, 65, 35, 156, 21, 118, 187, 170, 24, 47, 160, 199, 235, 44, 83, 234, 111, 254, 109, 13, 68, 39, 246, 60, 176, 34, 20, 16, 27, 11, 200, 141, 51, 193, 180, 51, 44, 226, 163, 99, 224, 129, 1, 56, 246, 75, 21, 194, 227, 194, 110, 81, 213, 96, 163, 44, 177, 191, 64, 244, 189, 98, 61, 54, 93, 154, 34, 157, 158, 54, 143, 195, 199, 117, 238, 0, 220, 243, 14, 230, 48, 195, 52, 167, 55, 58, 128, 112, 65, 8, 189, 91, 247, 169, 216, 85, 2, 151, 239, 150, 208, 31, 172, 63, 239, 173, 6, 23, 232, 200, 41, 133, 213, 217, 7, 251, 142, 244, 237, 61, 22, 122, 215, 236, 62, 212, 54, 42, 171, 152, 116, 9, 254, 99, 14, 216, 165, 126, 205, 29, 37, 44, 186, 95, 75, 158, 44, 33, 42, 217, 131, 151, 91, 75, 96, 42, 128, 71, 123, 184, 167, 45, 178, 123, 242, 85, 15, 119, 73, 11, 178, 189, 23, 0, 179, 204, 32, 248, 167, 0, 144, 128, 254, 180, 70, 122, 67, 218, 183, 211, 62, 172, 8, 66, 211, 5, 233, 200, 60, 235, 8, 8, 151, 133, 217, 24, 55, 152, 157, 208, 2, 98, 115, 129, 240, 99, 33, 212, 174, 10, 241, 225, 49, 176, 162, 61, 166, 167, 250, 182, 130, 122, 95, 38, 106, 238, 101, 7, 243, 249, 225, 181, 101, 119, 175, 3, 82, 0, 65, 182, 151, 70, 28, 35, 224, 127, 220, 236, 52, 213, 148, 98, 105, 203, 221, 50, 250, 155, 226, 90, 229, 91, 115, 214, 107, 16, 248, 39, 252, 186, 103, 7, 99, 33, 67, 215, 55, 104, 132, 31, 9, 251, 15, 17, 90, 88, 165, 80, 147, 21, 194, 43, 251, 63, 47, 174, 62, 168, 16, 157, 28, 13, 189, 68, 50, 13, 136, 174, 137, 32, 59, 178, 97, 51, 203, 12, 210, 61, 210, 30, 239, 107, 93, 154, 36, 3, 166, 235, 81, 12, 194, 199, 4, 191, 8, 122, 20, 243, 30, 167, 78, 48, 248, 231, 215, 245, 172, 0, 192, 45, 119, 253, 59, 211, 174, 239, 154, 216, 252, 93, 118, 81, 33, 224, 114, 82, 207, 102, 163, 246, 82, 77, 193, 167, 58, 161, 135, 76, 104, 151, 226, 158, 220, 31, 90, 231, 140, 205, 181, 38, 15, 150, 245, 52, 13, 76, 234, 99, 28, 103, 11, 168, 109, 235, 34, 245, 138, 131, 59, 123, 100, 68, 33, 216, 55, 128, 254, 160, 238, 211, 7, 168, 173, 20, 194, 31, 183, 73, 15, 136, 14, 32, 56, 186, 193, 225, 255, 108, 4, 118, 93, 223, 11, 164, 247, 165, 121, 186, 21, 93, 18, 65, 158, 36, 155, 178, 103, 185, 169, 204, 43, 127, 254, 230, 209, 93, 22, 106, 153, 111, 237, 178, 173, 11, 36, 212, 123, 179, 185, 105, 159, 179, 131, 14, 120, 71, 196, 14, 220, 218, 251, 163, 49, 145, 161, 139, 19, 68, 150, 153, 119, 253, 222, 151, 28, 210, 155, 82, 184, 219, 28, 252, 42, 15, 177, 139, 128, 216, 78, 64, 253, 163, 130, 158, 166, 33, 194, 190, 7, 194, 191, 233, 97, 87, 89, 184, 229, 14, 238, 119, 14, 238, 1, 7, 188, 8, 136, 29, 4, 196, 52, 1, 189, 175, 206, 69, 64, 239, 162, 145, 206, 76, 251, 60, 62, 208, 181, 150, 109, 255, 207, 194, 44, 50, 112, 119, 184, 193, 31, 55, 152, 2, 68, 63, 139, 32, 55, 171, 139, 249, 195, 6, 201, 254, 73, 143, 147, 36, 223, 77, 109, 1, 251, 227, 177, 117, 244, 108, 173, 153, 12, 200, 13, 235, 153, 231, 107, 3, 27, 91, 113, 136, 64, 240, 161, 250, 6, 160, 196, 35, 93, 148, 194, 45, 174, 63, 239, 87, 144, 109, 24, 220, 73, 64, 110, 43, 33, 223, 47, 251, 157, 55, 61, 126, 199, 134, 197, 103, 252, 211, 125, 223, 151, 191, 217, 103, 229, 52, 5, 200, 119, 52, 139, 182, 191, 222, 195, 95, 225, 33, 198, 139, 108, 14, 140, 67, 55, 231, 174, 183, 107, 54, 39, 181, 187, 234, 150, 201, 203, 153, 178, 88, 2, 120, 162, 117, 115, 195, 255, 212, 195, 158, 99, 161, 182, 81, 16, 235, 11, 168, 51, 21, 236, 241, 61, 95, 95, 31, 175, 243, 123, 48, 75, 70, 176, 122, 36, 178, 172, 210, 252, 206, 192, 46, 177, 112, 119, 57, 248, 23, 61, 228, 65, 18, 250, 227, 26, 122, 135, 186, 77, 127, 64, 195, 156, 102, 224, 46, 30, 221, 236, 83, 207, 213, 144, 239, 172, 251, 142, 85, 22, 118, 206, 200, 216, 114, 58, 59, 133, 88, 36, 160, 119, 210, 144, 27, 73, 148, 230, 150, 96, 102, 27, 200, 247, 74, 200, 77, 101, 102, 43, 243, 83, 152, 143, 142, 126, 229, 111, 200, 190, 181, 3, 16, 211, 5, 196, 84, 1, 125, 128, 134, 222, 41, 11, 248, 220, 95, 29, 146, 175, 38, 109, 105, 7, 254, 53, 15, 108, 146, 157, 138, 193, 135, 0, 44, 93, 199, 4, 61, 56, 62, 200, 175, 100, 159, 177, 136, 15, 137, 129, 149, 13, 3, 176, 162, 216, 248, 165, 158, 87, 16, 155, 245, 225, 152, 31, 6, 170, 227, 122, 110, 96, 226, 159, 245, 240, 55, 123, 36, 72, 128, 223, 34, 47, 221, 201, 3, 36, 236, 252, 222, 141, 205, 215, 60, 146, 235, 18, 216, 19, 214, 210, 32, 59, 128, 232, 23, 17, 212, 164, 44, 154, 51, 203, 13, 146, 131, 146, 30, 163, 117, 177, 85, 241, 219, 220, 95, 221, 128, 150, 3, 70, 205, 24, 55, 150, 3, 106, 92, 19, 255, 103, 12, 251, 217, 190, 199, 78, 205, 41, 118, 231, 219, 223, 15, 108, 156, 229, 244, 6, 113, 123, 192, 118, 91, 154, 240, 43, 61, 252, 252, 108, 222, 12, 185, 106, 0, 192, 63, 222, 191, 163, 241, 137, 207, 155, 93, 96, 10, 154, 74, 191, 118, 149, 133, 254, 128, 134, 40, 9, 200, 227, 36, 220, 165, 197, 125, 201, 47, 201, 44, 144, 243, 128, 249, 189, 129, 222, 89, 103, 209, 127, 7, 128, 213, 13, 191, 121, 199, 134, 138, 193, 111, 90, 43, 88, 230, 118, 3, 181, 77, 54, 71, 245, 126, 186, 199, 101, 1, 76, 170, 103, 46, 245, 223, 106, 190, 51, 114, 162, 96, 159, 179, 72, 206, 74, 224, 175, 111, 126, 14, 238, 81, 135, 228, 194, 4, 226, 49, 145, 245, 98, 0, 160, 143, 208, 72, 46, 78, 70, 207, 56, 118, 5, 130, 195, 235, 217, 185, 7, 210, 255, 28, 193, 74, 219, 106, 32, 217, 57, 1, 30, 200, 130, 27, 104, 64, 127, 40, 123, 102, 230, 65, 131, 244, 130, 180, 219, 102, 185, 46, 59, 30, 104, 3, 168, 150, 5, 146, 67, 240, 173, 193, 226, 0, 193, 190, 65, 55, 251, 179, 15, 89, 164, 103, 164, 240, 75, 124, 91, 218, 129, 125, 216, 102, 182, 45, 1, 253, 25, 13, 179, 180, 125, 150, 84, 135, 94, 114, 159, 4, 168, 169, 197, 154, 78, 242, 149, 164, 73, 204, 135, 205, 57, 44, 47, 30, 146, 152, 208, 119, 230, 102, 150, 152, 181, 23, 115, 0, 225, 109, 97, 94, 154, 177, 79, 88, 36, 7, 39, 77, 78, 186, 73, 208, 27, 74, 181, 254, 173, 191, 143, 93, 210, 226, 112, 129, 112, 118, 166, 156, 238, 207, 14, 230, 220, 129, 77, 112, 95, 45, 198, 71, 108, 58, 60, 229, 171, 166, 178, 216, 64, 230, 101, 195, 173, 139, 45, 69, 175, 115, 78, 238, 214, 108, 58, 106, 70, 189, 116, 247, 162, 131, 153, 95, 156, 21, 126, 251, 166, 183, 174, 160, 208, 119, 250, 166, 128, 160, 37, 54, 241, 85, 11, 255, 183, 108, 76, 213, 123, 85, 83, 169, 54, 255, 254, 51, 85, 94, 30, 181, 191, 179, 35, 154, 93, 184, 21, 174, 155, 152, 55, 101, 166, 63, 44, 68, 115, 180, 79, 121, 4, 223, 8, 178, 12, 12, 89, 128, 54, 162, 213, 130, 73, 64, 248, 191, 33, 244, 7, 116, 38, 112, 79, 22, 243, 78, 109, 171, 32, 182, 238, 221, 86, 214, 102, 67, 234, 144, 130, 200, 33, 250, 214, 110, 215, 187, 223, 192, 252, 210, 172, 181, 152, 143, 132, 29, 152, 115, 13, 220, 139, 217, 124, 8, 142, 104, 175, 86, 176, 67, 182, 26, 249, 137, 162, 20, 106, 87, 217, 30, 143, 89, 172, 181, 51, 158, 37, 160, 127, 172, 17, 220, 19, 32, 122, 34, 66, 233, 197, 18, 202, 107, 202, 40, 87, 203, 136, 62, 21, 13, 188, 206, 48, 132, 91, 10, 127, 83, 156, 63, 181, 79, 91, 196, 71, 196, 125, 55, 74, 249, 123, 233, 73, 50, 41, 107, 156, 163, 255, 75, 163, 244, 147, 18, 196, 134, 2, 238, 143, 14, 241, 39, 6, 190, 161, 201, 223, 237, 179, 13, 64, 117, 195, 139, 158, 140, 160, 46, 94, 187, 221, 236, 173, 155, 116, 141, 10, 244, 54, 65, 186, 173, 33, 35, 159, 252, 54, 161, 174, 7, 181, 246, 247, 22, 238, 155, 14, 254, 245, 108, 210, 233, 189, 154, 39, 103, 215, 146, 77, 43, 215, 207, 115, 222, 0, 204, 125, 69, 68, 162, 63, 214, 221, 48, 244, 254, 197, 191, 153, 27, 218, 107, 179, 166, 251, 15, 151, 7, 193, 114, 99, 153, 85, 55, 70, 99, 10, 204, 20, 208, 211, 117, 30, 224, 165, 151, 140, 96, 118, 190, 25, 16, 45, 140, 160, 167, 105, 248, 215, 61, 106, 167, 212, 16, 111, 27, 35, 185, 49, 1, 60, 32, 214, 19, 136, 254, 45, 106, 62, 105, 177, 89, 195, 231, 171, 35, 60, 88, 45, 142, 31, 130, 189, 2, 148, 46, 44, 33, 122, 54, 130, 56, 90, 180, 167, 29, 60, 11, 196, 71, 199, 176, 255, 103, 33, 198, 9, 148, 174, 42, 65, 207, 211, 16, 199, 138, 209, 245, 93, 104, 65, 201, 93, 108, 222, 80, 98, 126, 190, 53, 78, 74, 158, 36, 17, 124, 33, 128, 218, 74, 141, 170, 64, 6, 119, 4, 121, 169, 203, 62, 103, 17, 31, 21, 247, 155, 229, 249, 191, 52, 100, 157, 235, 181, 183, 186, 175, 109, 99, 153, 224, 87, 1, 130, 131, 138, 82, 153, 127, 195, 35, 249, 105, 2, 51, 199, 244, 90, 185, 232, 113, 172, 238, 244, 72, 127, 157, 230, 215, 82, 219, 168, 172, 84, 118, 74, 214, 33, 203, 189, 232, 224, 158, 116, 176, 215, 218, 181, 238, 177, 238, 211, 172, 9, 68, 238, 248, 250, 235, 90, 215, 224, 39, 253, 115, 205, 223, 233, 231, 121, 184, 191, 56, 200, 9, 197, 198, 29, 0, 16, 255, 146, 237, 196, 7, 0, 179, 32, 115, 14, 246, 113, 11, 189, 187, 206, 75, 200, 0, 32, 254, 89, 64, 188, 163, 30, 252, 62, 57, 60, 235, 177, 230, 135, 6, 193, 140, 0, 80, 128, 218, 89, 53, 173, 241, 201, 47, 73, 168, 45, 26, 54, 28, 253, 71, 251, 181, 13, 245, 175, 249, 204, 110, 36, 32, 118, 20, 163, 210, 84, 36, 56, 35, 200, 147, 148, 116, 105, 10, 255, 211, 145, 187, 7, 61, 87, 231, 187, 216, 147, 107, 19, 248, 43, 179, 239, 54, 179, 12, 252, 149, 30, 209, 113, 17, 68, 40, 16, 157, 26, 33, 222, 40, 134, 61, 206, 54, 47, 243, 189, 58, 118, 90, 193, 166, 211, 83, 164, 72, 179, 110, 119, 147, 0, 249, 15, 18, 250, 64, 13, 53, 73, 65, 109, 169, 80, 186, 172, 132, 234, 51, 85, 224, 254, 246, 179, 3, 191, 196, 35, 222, 49, 134, 250, 142, 66, 120, 100, 136, 240, 168, 16, 56, 170, 254, 187, 238, 234, 126, 242, 105, 204, 100, 232, 93, 101, 41, 160, 53, 37, 102, 121, 126, 182, 9, 68, 109, 61, 186, 98, 174, 166, 40, 4, 251, 23, 162, 37, 199, 75, 136, 41, 253, 223, 144, 255, 131, 111, 250, 12, 118, 253, 251, 72, 216, 125, 167, 31, 148, 152, 231, 70, 125, 112, 138, 100, 94, 210, 60, 119, 52, 32, 55, 201, 94, 130, 16, 254, 107, 136, 242, 162, 50, 130, 37, 65, 159, 59, 86, 123, 165, 97, 25, 86, 236, 208, 207, 243, 27, 135, 66, 252, 45, 122, 172, 52, 184, 103, 50, 227, 23, 227, 5, 196, 161, 217, 223, 170, 35, 235, 229, 246, 213, 14, 254, 170, 186, 3, 190, 187, 94, 118, 223, 64, 64, 158, 147, 153, 153, 220, 183, 97, 253, 252, 222, 225, 113, 188, 126, 190, 135, 89, 81, 255, 238, 72, 64, 159, 92, 196, 236, 250, 163, 13, 89, 201, 157, 109, 122, 148, 178, 241, 182, 54, 24, 133, 236, 252, 11, 34, 63, 186, 232, 171, 30, 230, 27, 35, 56, 78, 29, 200, 131, 91, 191, 198, 119, 123, 151, 131, 253, 156, 69, 237, 223, 107, 217, 82, 149, 2, 162, 99, 35, 232, 27, 53, 196, 7, 27, 4, 125, 213, 216, 123, 15, 129, 95, 226, 225, 175, 241, 176, 39, 90, 196, 239, 139, 243, 96, 87, 140, 23, 8, 206, 14, 218, 215, 14, 222, 0, 208, 217, 250, 42, 197, 168, 10, 58, 26, 2, 145, 181, 217, 133, 220, 196, 228, 250, 25, 116, 93, 24, 183, 93, 97, 145, 220, 152, 32, 190, 44, 70, 237, 172, 26, 170, 199, 85, 81, 61, 176, 138, 248, 135, 195, 219, 120, 165, 43, 80, 113, 175, 184, 220, 49, 71, 223, 233, 191, 119, 178, 191, 206, 195, 191, 225, 115, 97, 82, 199, 42, 172, 107, 164, 7, 167, 232, 220, 166, 19, 213, 227, 170, 72, 110, 74, 50, 231, 114, 66, 132, 232, 241, 104, 173, 74, 78, 102, 182, 65, 117, 106, 21, 241, 220, 24, 233, 255, 164, 217, 210, 205, 219, 4, 62, 216, 59, 64, 180, 96, 240, 13, 80, 186, 214, 210, 0, 64, 108, 211, 79, 47, 247, 253, 68, 110, 17, 238, 181, 158, 29, 99, 211, 58, 250, 129, 217, 31, 171, 157, 235, 209, 254, 163, 197, 255, 185, 75, 93, 22, 228, 0, 80, 211, 179, 255, 151, 219, 202, 60, 248, 25, 206, 236, 216, 220, 210, 80, 110, 220, 59, 51, 38, 177, 143, 128, 218, 169, 190, 126, 255, 166, 135, 61, 191, 77, 79, 95, 52, 54, 77, 89, 62, 242, 158, 50, 252, 66, 152, 207, 129, 116, 81, 58, 162, 111, 223, 147, 159, 146, 133, 223, 249, 75, 47, 13, 144, 190, 238, 80, 155, 83, 131, 95, 227, 1, 1, 132, 51, 67, 132, 167, 22, 59, 63, 237, 173, 99, 255, 84, 141, 249, 85, 49, 127, 187, 108, 166, 237, 236, 96, 51, 32, 124, 36, 204, 244, 170, 4, 36, 11, 19, 84, 63, 87, 69, 231, 118, 157, 163, 150, 157, 183, 68, 208, 253, 154, 6, 135, 57, 113, 104, 130, 174, 78, 84, 249, 132, 246, 127, 243, 168, 126, 166, 138, 120, 187, 24, 102, 86, 246, 230, 49, 119, 190, 131, 191, 218, 195, 47, 242, 192, 8, 204, 219, 100, 126, 130, 218, 129, 53, 184, 23, 50, 227, 146, 29, 18, 225, 143, 194, 108, 247, 115, 31, 216, 103, 139, 155, 107, 108, 92, 176, 78, 177, 18, 240, 87, 123, 152, 153, 6, 181, 83, 178, 172, 65, 77, 81, 136, 230, 175, 101, 215, 177, 103, 1, 251, 101, 139, 116, 191, 20, 241, 86, 49, 170, 235, 87, 81, 61, 177, 138, 244, 174, 52, 95, 203, 86, 219, 169, 65, 119, 86, 235, 10, 200, 0, 64, 238, 212, 247, 103, 229, 158, 197, 255, 251, 87, 123, 118, 228, 141, 141, 60, 228, 246, 18, 98, 186, 40, 202, 119, 119, 52, 76, 202, 213, 197, 177, 180, 174, 245, 117, 249, 222, 97, 92, 63, 111, 188, 199, 179, 92, 94, 122, 149, 29, 18, 242, 60, 9, 245, 69, 149, 7, 220, 102, 153, 105, 155, 214, 188, 77, 76, 42, 142, 65, 249, 183, 124, 247, 229, 173, 134, 71, 34, 74, 173, 47, 223, 201, 111, 201, 124, 119, 180, 95, 227, 97, 206, 24, 217, 42, 70, 227, 198, 208, 190, 126, 159, 191, 210, 163, 246, 169, 26, 220, 159, 234, 207, 184, 225, 104, 157, 191, 166, 151, 0, 100, 152, 199, 174, 165, 25, 123, 99, 16, 94, 17, 109, 105, 7, 225, 173, 33, 244, 84, 13, 31, 123, 196, 167, 199, 48, 135, 25, 248, 239, 251, 81, 111, 136, 52, 100, 65, 119, 15, 22, 206, 73, 109, 53, 180, 108, 180, 241, 56, 91, 186, 36, 237, 125, 114, 142, 68, 148, 248, 136, 129, 57, 210, 0, 15, 3, 241, 103, 227, 236, 8, 26, 178, 205, 91, 225, 13, 97, 159, 45, 42, 187, 214, 81, 129, 172, 116, 28, 220, 186, 142, 138, 122, 151, 1, 94, 229, 145, 222, 154, 69, 165, 106, 138, 234, 183, 45, 239, 128, 175, 251, 61, 143, 116, 122, 154, 191, 97, 10, 0, 228, 206, 131, 20, 244, 21, 13, 243, 115, 183, 126, 218, 5, 239, 81, 252, 191, 123, 186, 103, 209, 245, 55, 251, 60, 72, 80, 91, 42, 200, 163, 101, 246, 62, 231, 53, 190, 219, 78, 104, 187, 52, 19, 116, 57, 65, 66, 158, 34, 33, 55, 169, 59, 222, 39, 134, 63, 26, 53, 247, 54, 100, 39, 135, 233, 98, 115, 158, 3, 204, 53, 237, 89, 110, 87, 167, 171, 166, 62, 230, 221, 104, 216, 238, 33, 58, 90, 47, 74, 225, 39, 139, 76, 55, 249, 229, 200, 156, 214, 105, 154, 91, 157, 13, 203, 117, 239, 146, 249, 146, 78, 111, 243, 176, 118, 68, 173, 41, 96, 109, 172, 16, 141, 244, 216, 181, 84, 148, 26, 186, 59, 14, 117, 25, 119, 56, 236, 64, 93, 168, 242, 214, 222, 230, 78, 3, 119, 121, 251, 44, 115, 12, 61, 67, 191, 214, 231, 89, 186, 216, 80, 64, 255, 172, 247, 125, 118, 242, 60, 57, 224, 151, 9, 244, 249, 170, 203, 169, 67, 43, 197, 12, 136, 6, 3, 240, 183, 122, 196, 95, 137, 115, 131, 211, 59, 232, 162, 135, 113, 79, 34, 114, 174, 131, 93, 213, 144, 165, 31, 20, 32, 88, 20, 12, 108, 215, 238, 46, 128, 158, 175, 17, 61, 21, 97, 44, 97, 175, 180, 121, 22, 160, 246, 110, 237, 50, 67, 99, 182, 236, 205, 224, 12, 220, 254, 220, 22, 25, 254, 54, 10, 242, 188, 158, 231, 141, 60, 69, 54, 189, 127, 218, 220, 222, 187, 177, 119, 173, 163, 203, 119, 203, 252, 44, 171, 121, 172, 251, 223, 219, 239, 90, 248, 184, 62, 103, 142, 45, 26, 42, 185, 123, 220, 200, 60, 143, 174, 134, 99, 59, 232, 108, 215, 56, 178, 126, 246, 125, 29, 29, 27, 45, 196, 44, 129, 240, 163, 133, 160, 118, 237, 65, 104, 26, 247, 63, 53, 4, 103, 59, 168, 94, 237, 73, 205, 85, 208, 187, 15, 110, 191, 175, 250, 145, 202, 55, 54, 186, 23, 93, 175, 205, 72, 134, 85, 208, 239, 245, 69, 38, 173, 129, 240, 252, 176, 79, 159, 161, 207, 214, 144, 19, 139, 249, 28, 30, 22, 246, 218, 183, 126, 56, 199, 174, 165, 243, 224, 147, 2, 193, 33, 133, 111, 117, 43, 93, 219, 217, 65, 215, 18, 26, 0, 152, 159, 180, 87, 112, 220, 146, 39, 103, 238, 51, 249, 67, 8, 63, 18, 66, 108, 44, 96, 126, 97, 224, 239, 246, 16, 59, 10, 200, 3, 36, 244, 62, 186, 223, 12, 222, 61, 230, 128, 35, 235, 34, 184, 71, 0, 191, 192, 195, 222, 108, 225, 31, 240, 16, 27, 9, 136, 221, 5, 212, 222, 10, 122, 15, 61, 226, 59, 200, 253, 85, 30, 241, 59, 99, 148, 206, 45, 1, 65, 253, 254, 110, 242, 48, 71, 244, 252, 64, 147, 115, 18, 148, 174, 42, 101, 103, 29, 5, 16, 28, 16, 64, 61, 161, 96, 238, 53, 112, 247, 57, 248, 7, 235, 175, 79, 221, 86, 64, 76, 22, 144, 59, 74, 200, 237, 101, 118, 206, 52, 20, 77, 6, 56, 38, 178, 244, 197, 62, 219, 161, 188, 161, 104, 106, 183, 218, 231, 228, 187, 94, 67, 239, 173, 179, 215, 41, 62, 233, 224, 159, 242, 217, 43, 21, 87, 122, 96, 203, 108, 151, 179, 218, 87, 65, 239, 91, 188, 45, 205, 45, 25, 220, 184, 248, 133, 62, 107, 244, 178, 75, 214, 132, 40, 58, 45, 66, 58, 37, 45, 230, 213, 246, 2, 234, 112, 133, 224, 136, 134, 230, 72, 43, 45, 252, 21, 189, 27, 187, 125, 36, 219, 193, 14, 13, 168, 247, 215, 203, 237, 119, 245, 32, 0, 43, 179, 107, 233, 29, 138, 46, 104, 254, 45, 15, 119, 217, 240, 63, 91, 127, 167, 135, 89, 110, 186, 189, 242, 179, 113, 93, 113, 196, 157, 205, 238, 26, 184, 13, 176, 247, 217, 172, 217, 212, 114, 15, 177, 155, 128, 250, 176, 66, 112, 80, 113, 238, 219, 173, 118, 176, 103, 116, 31, 79, 183, 208, 1, 115, 50, 175, 37, 39, 74, 132, 191, 14, 145, 94, 153, 194, 255, 79, 246, 26, 98, 121, 176, 132, 158, 174, 243, 179, 254, 3, 102, 74, 182, 22, 157, 219, 238, 181, 163, 211, 208, 198, 223, 154, 157, 57, 239, 234, 121, 161, 182, 83, 40, 61, 88, 66, 186, 32, 133, 91, 148, 217, 135, 216, 77, 64, 237, 167, 160, 167, 235, 226, 8, 228, 75, 14, 98, 130, 200, 118, 191, 159, 24, 33, 22, 49, 236, 73, 118, 100, 198, 110, 128, 4, 75, 2, 168, 73, 10, 246, 105, 11, 247, 148, 131, 127, 186, 110, 235, 171, 50, 141, 16, 83, 235, 157, 68, 247, 210, 249, 146, 128, 143, 253, 144, 171, 73, 195, 97, 7, 93, 75, 28, 254, 45, 15, 63, 175, 189, 130, 227, 150, 8, 122, 122, 86, 10, 181, 187, 130, 220, 40, 43, 63, 6, 7, 4, 8, 14, 232, 37, 131, 245, 232, 117, 247, 186, 251, 154, 131, 251, 180, 203, 122, 21, 43, 32, 60, 52, 4, 14, 197, 160, 175, 51, 92, 184, 243, 28, 226, 142, 56, 219, 8, 33, 129, 240, 240, 16, 254, 106, 15, 251, 233, 238, 206, 199, 223, 224, 17, 111, 17, 35, 58, 43, 130, 216, 160, 254, 194, 142, 141, 36, 194, 195, 67, 224, 112, 172, 147, 248, 154, 135, 128, 104, 234, 206, 214, 95, 125, 72, 110, 82, 47, 69, 79, 31, 64, 224, 184, 204, 116, 123, 81, 197, 128, 230, 231, 220, 20, 234, 7, 217, 251, 163, 69, 40, 50, 231, 61, 179, 151, 223, 16, 123, 36, 151, 247, 237, 208, 221, 2, 7, 124, 166, 62, 255, 68, 182, 185, 198, 125, 187, 151, 77, 116, 247, 219, 92, 204, 129, 193, 173, 159, 15, 180, 147, 31, 0, 216, 63, 88, 196, 91, 54, 111, 20, 53, 243, 155, 29, 153, 251, 139, 131, 61, 125, 244, 54, 77, 137, 13, 5, 130, 3, 3, 4, 7, 246, 94, 221, 242, 137, 71, 114, 126, 207, 93, 24, 177, 52, 235, 148, 214, 85, 21, 209, 59, 104, 232, 239, 233, 94, 159, 99, 126, 98, 161, 63, 177, 185, 48, 104, 58, 78, 232, 206, 25, 189, 96, 58, 185, 40, 65, 233, 138, 82, 158, 176, 200, 205, 101, 230, 111, 78, 236, 101, 46, 190, 224, 16, 31, 19, 67, 252, 147, 64, 233, 244, 236, 245, 191, 209, 231, 35, 196, 50, 134, 253, 130, 29, 246, 177, 27, 140, 210, 200, 205, 37, 228, 230, 3, 179, 117, 120, 32, 185, 46, 105, 73, 95, 147, 150, 219, 65, 80, 248, 187, 118, 163, 53, 117, 235, 71, 129, 248, 244, 184, 105, 51, 67, 119, 175, 10, 36, 243, 146, 188, 195, 78, 111, 196, 103, 198, 77, 27, 237, 122, 116, 94, 143, 91, 36, 243, 70, 39, 138, 182, 39, 89, 36, 63, 47, 190, 59, 58, 38, 130, 186, 176, 151, 50, 215, 133, 14, 181, 163, 107, 48, 143, 154, 129, 191, 176, 196, 103, 13, 108, 210, 159, 142, 193, 151, 186, 12, 210, 15, 250, 55, 252, 128, 143, 124, 152, 101, 6, 201, 63, 175, 221, 51, 247, 215, 123, 196, 231, 197, 253, 246, 152, 247, 111, 122, 196, 223, 142, 251, 204, 206, 1, 192, 223, 230, 225, 86, 55, 172, 93, 174, 176, 189, 190, 180, 195, 94, 99, 155, 142, 98, 141, 196, 250, 121, 99, 0, 234, 94, 42, 238, 211, 220, 51, 186, 229, 65, 159, 12, 96, 252, 191, 25, 247, 121, 2, 32, 249, 114, 210, 119, 245, 42, 5, 146, 155, 146, 30, 75, 246, 61, 6, 25, 7, 9, 232, 253, 138, 117, 213, 228, 187, 201, 232, 142, 209, 181, 30, 241, 153, 113, 211, 218, 120, 111, 126, 194, 220, 111, 80, 59, 188, 6, 191, 216, 195, 157, 237, 16, 95, 30, 231, 239, 34, 136, 62, 27, 65, 93, 161, 134, 117, 236, 6, 197, 235, 131, 24, 131, 78, 143, 248, 123, 113, 203, 150, 61, 134, 205, 14, 218, 176, 17, 104, 203, 22, 162, 253, 213, 30, 213, 15, 87, 145, 222, 153, 102, 147, 49, 205, 38, 136, 91, 237, 144, 46, 78, 81, 253, 88, 21, 102, 118, 255, 3, 233, 175, 243, 168, 29, 85, 67, 186, 56, 205, 54, 162, 89, 0, 166, 190, 235, 116, 153, 65, 237, 171, 53, 196, 219, 247, 47, 250, 195, 137, 249, 152, 65, 186, 184, 171, 197, 25, 16, 158, 28, 66, 158, 214, 243, 80, 250, 133, 30, 201, 142, 9, 170, 199, 87, 145, 222, 150, 194, 62, 109, 225, 95, 243, 153, 115, 115, 245, 35, 76, 175, 56, 152, 71, 12, 146, 255, 78, 80, 253, 151, 42, 226, 201, 113, 143, 37, 199, 117, 13, 123, 188, 69, 245, 152, 42, 146, 27, 19, 216, 39, 44, 252, 154, 250, 184, 248, 204, 249, 187, 87, 92, 246, 204, 207, 174, 33, 153, 150, 244, 223, 20, 166, 47, 163, 190, 192, 161, 122, 96, 21, 201, 205, 9, 220, 31, 235, 71, 202, 92, 253, 21, 166, 47, 58, 164, 183, 165, 168, 29, 89, 27, 112, 118, 102, 159, 41, 158, 143, 253, 77, 31, 207, 234, 254, 230, 191, 29, 174, 243, 231, 189, 162, 10, 103, 109, 175, 24, 221, 57, 149, 254, 60, 69, 237, 252, 26, 204, 114, 147, 117, 210, 179, 245, 231, 252, 178, 67, 122, 71, 138, 218, 161, 53, 184, 243, 250, 25, 159, 165, 64, 237, 208, 26, 210, 91, 83, 184, 151, 93, 22, 44, 165, 89, 67, 149, 116, 73, 138, 234, 199, 171, 48, 51, 7, 238, 176, 131, 179, 131, 188, 196, 107, 30, 50, 253, 6, 115, 35, 18, 136, 93, 238, 80, 219, 163, 134, 228, 39, 73, 230, 47, 222, 170, 143, 85, 213, 195, 253, 185, 238, 79, 79, 170, 34, 217, 61, 105, 122, 55, 187, 61, 213, 34, 254, 65, 156, 5, 214, 93, 162, 254, 93, 53, 108, 99, 55, 168, 103, 127, 112, 138, 234, 167, 171, 72, 230, 37, 48, 143, 26, 184, 151, 93, 118, 158, 222, 213, 253, 251, 235, 30, 118, 101, 150, 168, 85, 15, 168, 54, 87, 23, 214, 49, 59, 24, 214, 42, 88, 123, 198, 25, 100, 44, 18, 253, 33, 130, 218, 66, 193, 191, 238, 81, 125, 71, 149, 3, 50, 202, 168, 139, 20, 162, 211, 178, 205, 149, 230, 65, 131, 100, 215, 132, 131, 66, 104, 7, 67, 180, 131, 210, 171, 37, 200, 9, 18, 238, 37, 135, 218, 38, 181, 182, 250, 173, 146, 143, 155, 180, 172, 74, 83, 95, 114, 17, 227, 4, 48, 141, 227, 49, 218, 232, 195, 26, 118, 237, 207, 51, 28, 16, 66, 59, 24, 170, 29, 76, 46, 94, 173, 220, 231, 18, 51, 5, 157, 140, 117, 220, 242, 122, 185, 84, 0, 122, 142, 230, 128, 140, 34, 226, 120, 1, 53, 185, 222, 146, 246, 5, 7, 119, 145, 227, 160, 16, 218, 193, 16, 237, 64, 127, 77, 23, 167, 97, 30, 107, 191, 210, 61, 189, 46, 105, 25, 230, 252, 236, 248, 162, 24, 47, 16, 30, 17, 2, 11, 0, 59, 207, 194, 223, 229, 135, 180, 254, 77, 6, 79, 240, 201, 32, 63, 5, 146, 254, 186, 255, 13, 150, 98, 134, 64, 249, 246, 114, 203, 190, 191, 122, 92, 21, 254, 234, 117, 119, 53, 143, 227, 181, 110, 218, 65, 143, 116, 0, 226, 0, 1, 53, 75, 33, 252, 112, 118, 132, 199, 191, 238, 97, 46, 110, 191, 170, 23, 51, 116, 210, 58, 86, 0, 241, 55, 227, 108, 195, 147, 206, 142, 29, 150, 127, 82, 70, 229, 249, 10, 42, 190, 210, 109, 215, 45, 25, 38, 246, 4, 212, 63, 20, 239, 93, 183, 23, 91, 142, 9, 161, 29, 12, 210, 14, 212, 92, 133, 138, 175, 160, 242, 114, 5, 229, 235, 202, 89, 146, 162, 235, 167, 49, 254, 61, 6, 30, 104, 191, 159, 204, 12, 157, 180, 20, 119, 169, 67, 237, 201, 26, 244, 169, 26, 106, 170, 202, 222, 56, 23, 112, 92, 70, 212, 168, 191, 164, 243, 115, 196, 230, 183, 102, 64, 253, 165, 253, 34, 143, 78, 209, 201, 193, 27, 32, 28, 175, 117, 211, 14, 122, 197, 0, 110, 141, 131, 125, 204, 194, 92, 106, 224, 23, 182, 103, 53, 133, 187, 220, 9, 33, 132, 144, 117, 0, 150, 220, 9, 33, 132, 16, 10, 58, 33, 132, 16, 66, 40, 232, 132, 16, 66, 8, 161, 160, 19, 66, 8, 33, 132, 130, 78, 8, 33, 132, 80, 208, 9, 33, 132, 16, 66, 65, 39, 132, 16, 66, 8, 5, 157, 16, 66, 8, 33, 20, 116, 66, 8, 33, 132, 130, 78, 8, 33, 132, 16, 10, 58, 33, 132, 16, 66, 40, 232, 132, 16, 66, 8, 161, 160, 19, 66, 8, 33, 20, 116, 66, 8, 33, 132, 80, 208, 9, 33, 132, 16, 66, 65, 39, 132, 16, 66, 8, 5, 157, 16, 66, 8, 161, 160, 19, 66, 8, 33, 132, 130, 78, 8, 33, 132, 16, 10, 58, 33, 132, 16, 66, 40, 232, 132, 16, 66, 8, 5, 157, 16, 66, 8, 33, 20, 116, 66, 8, 33, 132, 80, 208, 9, 33, 132, 16, 66, 65, 39, 132, 16, 66, 40, 232, 132, 16, 66, 8, 161, 160, 19, 66, 8, 33, 132, 130, 78, 8, 33, 132, 16, 10, 58, 33, 132, 16, 66, 65, 39, 132, 16, 66, 8, 5, 157, 16, 66, 8, 33, 20, 116, 66, 8, 33, 132, 80, 208, 9, 33, 132, 16, 10, 58, 33, 132, 16, 66, 40, 232, 132, 16, 66, 8, 161, 160, 19, 66, 8, 33, 132, 130, 78, 8, 33, 132, 80, 208, 9, 33, 132, 16, 66, 65, 39, 132, 16, 66, 200, 40, 162, 57, 4, 132, 16, 66, 200, 24, 33, 12, 128, 113, 235, 3, 149, 10, 80, 41, 67, 188, 99, 3, 160, 99, 34, 228, 166, 155, 80, 208, 9, 33, 132, 144, 182, 100, 242, 251, 32, 222, 179, 57, 196, 38, 239, 130, 24, 63, 30, 98, 194, 70, 144, 27, 140, 131, 88, 127, 125, 200, 119, 78, 132, 156, 184, 49, 212, 248, 13, 33, 42, 21, 0, 192, 255, 3, 181, 13, 159, 48, 164, 107, 200, 123, 0, 0, 0, 0, 73, 69, 78, 68, 174, 66, 96, 130]

print("Let's see how good your BASE is...")
count = 0

for i in range(175):
    txt = list(printable)
    shuffle(txt)
    question = 'What does this mean:\t'+b64encode(''.join(txt).encode()).decode('utf-8')
    print(question)
    if input('> ') != ''.join(txt):
        print("Sorry!")
        exit(0)
    else:
        print(datalist[(count*43):((count+1)*43)])
        count += 1
