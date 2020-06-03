<h1> Proyecto-PatoManuG- </h1>
<h3> Equipo </h3>
    <ul> 
        <li> Manuel Eduardo Torres Magdaleno </li>
        <li> Gabriel Sebastián Carrión Vivar </li>
    </ul>

<h2>Manual de usuario</h2>

<h3>¿Que se necesita tener instalado para ejecutar el compilador?</h3>

<p>Se necesita principalmente tener instalado python 3 (en adelante) y el analizador PLY (Python LEX and YACC) con las librerias:</p>

<ul>
  <li>Lex</li>
  <li>Yaac</li>
  <li>sys (Para la máquina virtual)</li>
</ul>

<h3>¿Cómo hacer un programa en nuestro lenguaje?</h3>

<p>A continuación se muestra un ejemplo de cómo se debe de declarar un programa en este lenguaje:</p>

#### Programa principal #### 
program spaceX;  

 #### Variables globales #### 
var   
int a;

## Función sin retorno
fun void Launch(int r, int f, int j1, int g23); {
  var
  int a, b, c[3];
    a = 10;
    b = 20;
    b = (a * b) + 7;
    c[1] = b + a;
    print(b);
}

### Función con retorno
fun int LAunch2 (int i, int i2); {
    var
    int k98, j99;
    k98 = 2;
    j99 = 10;
    return (k98 * j99);
}

## Este es el programa principal ###
main() {
    var 
        int i, j, k, l, m, d, x, y, ggg[3];
        char a1, b1;
        Launch(1, 2, 3, 4);
        
        k = i + k;
        l = i - j;
        m = i * l;
        ggg[2] = 12;
        a1 = 'e';
        b1 = 'f';

       x = 10;

        if(x != j){
            d = x / y;
        }

       if (d == k) {
           print("son iguales");
       }

        if (d >= k) {
           print("d es mayor");
       }

        else {
           print("HOLA MUNDO");
       }

     print (x+y);

    while(x<y){
        x = x+y;
    }
   

   for (from x = 10 to x <100){
       x = x + 2;
       print (x);
   }

   
        while (y == x) {
            print(1);
        }
}
end
 ##### Debe escribirse el “end” para terminar el programa ########

<h3>¿Como declarar variables?</h3>

##### Primero debe de escribirse “Var” ########
##### Seguido debe de ir el tipo de variable (int, float, char) ########
##### Por último, el nombre de dichas variables ########

Var 
int a, b, c;
float d, e, f;
char g, h, i;

<h3>¿Cómo declarar funciones?</h3>
<h4>Funciones sin retorno</h4>

fun void ejemplo_funcion(int r, int f, int j1, int g23); 
{
 ### Instrucciones aquí ### 
 }

 <h4>Funciones con retorno</h4>

 fun int Launch(int r, int f, int j1, int g23);
 {
 ### Instrucciones aquí ### 
 }

<h3>¿ Cómo se hace una condicional (un if) ?</h3>
<h4>if</h4>

if (x > j) {
## Escriba aqui instrucciones ## 
}


<h4>if else</h4>

if (x > j) {
## Escriba aqui instrucciones ## 
}

else
{
## Escriba instrucciones aquí ## 
}

<h3>¿Cómo se hacen ciclos?</h3>

<h4>While</h4>

    while(x<y) {
        x = x+y;
    }

<h4>For</h4>

   for (from x = 10 to x <100) {
       x = x + 2;
       print (x);
   }

<h3>¿Cómo se hacen prints?</h3>
<h4>Variables</h4>
<p>Suponiendo que tenemos declarada la variable entera ‘a’:</p>

print (a);

<h4>Expresiones</h4>
<p>Suponiendo que tenemos declarado como enteros a y b (por poner un ejemplo) sería:</p>

print (a + b);

<h4>String</h4>

print (“Hola mundo”);

