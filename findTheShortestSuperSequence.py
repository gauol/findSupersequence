import defs as d                    # import pliku z algorytmami

inputFile = "input.txt"             # nazwa pliku w którym zawarto sekwencje
outputFile = "out.txt"              # nazwa pliku wyjściowego

seqs = d.getSequences(inputFile)    # inicjacja tablicy z sekwencjami

result = d.dijkSuperstring(seqs)    # uruchomienie algorytmu szukanie najkrótszego superciągu

print(result)                       # wyświetlenie w konsoli wyniku

d.saveToFile(result, outputFile)    # zapis wyniku do pliku
