def rearrangeBarcodes(self, barcodes: list[int]) -> list[int]:
    from collections import Counter
    count = Counter(barcodes)
    sorted_barcodes = sorted(count.items(), key=lambda x: x[1], reverse=True)
    
    result = [0] * len(barcodes)
    index = 0
    
    for barcode, freq in sorted_barcodes:
        for _ in range(freq):
            result[index] = barcode
            index += 2
            if index >= len(barcodes):
                index = 1
    
    return result