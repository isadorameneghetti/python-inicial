x = int(input('Escolha o ponto x: '))
y = int(input('Escolha o ponto y: '))

if x>0 and y>0:
    print('O ponto está no primeiro quadrante')
elif x<0 and y>0:
    print('O ponto está no segundo quadrante')
elif x<0 and y<0:
    print('O ponto está no terceiro quadrante')
elif x>0 and y<0:
    print('O ponto está no quarto quadrante')
else:
    print('Digite um número válido')