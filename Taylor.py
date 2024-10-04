def taylor_ln(x,terms=10):
    if x<=0:
       raise ValueError ("el valor de x debe de ser mayor que 0")
    y=x-1
    if not (-1<y<=1):
       raise ValueError ("para una buena aproximacion, x debe estar cerca a 1")
       result=0
    for n in range(1,terms+1):
        resul+=((-1)**(n+1)*y**n)/n
    return result

    x=float (input("introduce el valor de x(>0):"))
    terms=int(input("introduce el numero de terminos a utilizar en la serie de taylor"))

    try:
        aprox=taylor_ln(x,terms)
        print(f"ln{x}={aprox} utilizando {terms} terminos de la serie de taylor")
    except ValueError as e:
        print(e)
              
