#!/bin/bash

echo "=== KALKULATOR BUNGA SEDERHANA ==="

# Input dari user
read -p "Masukkan pokok (modal awal): " principal
read -p "Masukkan suku bunga (%): " rate
read -p "Masukkan waktu (tahun): " time

# Hitung bunga sederhana
interest=$(echo "$principal * $rate * $time / 100" | bc)

# Hitung total akhir
total=$(echo "$principal + $interest" | bc)

echo "-----------------------------"
echo "Bunga: $interest"
echo "Total akhir: $total"
