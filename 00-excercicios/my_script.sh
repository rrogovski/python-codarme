#!/bin/bash
echo "Informe o nome do arquivo [default: exercicio]"
read filename
[[ ! -z "$filename" ]] && echo "Arquivo criado pelo script" >> "$filename.txt" || echo "Arquivo criado pelo script" >> "exercicio.txt"
[[ ! -z "$filename" ]] && echo  "$filename.txt criado com sucesso." || echo "exercicio.txt criado com sucesso."
