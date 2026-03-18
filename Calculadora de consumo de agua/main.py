{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3652cdfe-608b-4f5f-a20a-6fedf5d26017",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Insira o valor atual mostrado no relogio:  5399\n",
      "Insira o valor da ultima leitura:  5365\n",
      "Insira a taxa conforme o numero de familias:  10\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "O consumo foi de 34.00 m³\n",
      "O excedente foi de 4.00 m³\n",
      "O valor a pagar será: R$ 63.00\n"
     ]
    }
   ],
   "source": [
    "                                                    #### #CALCULO DE CONSUMO DE AGUA\n",
    "# 30 m == 1.50\n",
    "# < 30 m = 2.00\n",
    "#5399 - 5365\n",
    "#taxa = 10 reais por familia\n",
    "\n",
    "try:\n",
    "    valor_atual = float(input(\"Insira o valor atual mostrado no relogio: \"))\n",
    "    valor_anterior = float(input(\"Insira o valor da ultima leitura: \"))\n",
    "    taxa = float(input(\"Insira a taxa conforme o numero de familias: \"))\n",
    "\n",
    "    consumo = valor_atual - valor_anterior\n",
    "    excedente = consumo - 30\n",
    "\n",
    "    print(f\"O consumo foi de {consumo:.2f} m³\")\n",
    "    print(f\"O excedente foi de {max(0, excedente):.2f} m³\") # Garante que excedente não seja negativo\n",
    "\n",
    "    if consumo <= 30:\n",
    "        valor_a_pagar = consumo * 1.50 + taxa\n",
    "        print(f\"O valor a pagar será: R$ {valor_a_pagar:.2f}\")\n",
    "\n",
    "    elif consumo > 30:\n",
    "        valor_a_pagar = (30 * 1.50) + (excedente * 2.00) + taxa\n",
    "        print(f\"O valor a pagar será: R$ {valor_a_pagar:.2f}\")\n",
    "\n",
    "except ValueError:\n",
    "    print(\"Entrada inválida. Por favor, insira apenas números.\")\n",
    "except Exception as e:\n",
    "    print(f\"Ocorreu um erro inesperado: {e}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e6bef54f-e4be-410e-bf7e-390f2ab3384f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
