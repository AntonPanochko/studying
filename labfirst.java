import java.util.Arrays; 
import java.util.Random;
public class labfirst {
    public static void main(String[] args){ // public - метод открытый; static - статический метод, который напрямую относится к классу lab1; void - метод ничего не возращает; main - точка входа в программу 
// String[] args - это массив со строками, который можно передать при запуске программы 
// публичный, статичный метод под названием main, который ничего не возвращает, но может принимать в себя аргументы с массивом строк 
// внутри метода мы распечатываем строки 18, 25, 41. тк никаких аргументов больше нет, программа завершается          
        int[] n = new int[10];
        int number = 0;
        for (int i = 22; i >= 4; i--){
            if (i % 2 == 0){
                n[number] = i;
                number += 1;
            }
        }
        System.out.println("Массив n: " + Arrays.toString(n)); // Arrays.toString(n) преобразование массива в строку 

        float[] x = new float[18]; 
        Random random = new Random(); // создание генератора случайных чисел
        for (int i = 0; i < x.length; i++){
            x[i] = random.nextFloat() * 10.0f - 8.0f; // random.nextFloat() - случайное число от 0.0 до 1.0 ; * 10.0f - расширяем диапазон до 0.0 - 10.0 ; - 8.0f - сдвигает диапазон: 0.0-10.0 → -8.0-2.0
        }
        
        System.out.println("Массив x: " + Arrays.toString(x)); // то же самое, что и для массива n
        printArray(x, n);
    }
    static void printArray(float[] xArr, int [] nArr){
        double[][] l = new double[10][18];
        int[] checkMass =  {6, 10, 12, 16, 18};
        for (int m: checkMass){
            for (int i = 0; i < 10; i++){
                for (int j = 0; j < 18; j++){
                    if (nArr[i] == 22){
                        double arg = ((xArr[j] - 3) / 1) * Math.E + 1;
                        l[i][j] = Math.cbrt(Math.log(Math.acos(arg)));
                    }else if (nArr[i] == m){
                        double arg = ((xArr[j] - 3) / 1) * Math.E + 1;
                        l[i][j] = Math.atan(Math.pow(arg, 2));
                    }else{
                        l[i][j] = Math.pow(Math.E, Math.pow(Math.E, Math.pow(Math.pow(xArr[j], 4 / (1/3 + xArr[j])), Math.sin(xArr[j]) * (4 - Math.cos(xArr[j])))));
                    }
                }
            } 
        }
        System.out.println("Результирующий массив l:");
        getAnswer(l);
    }
    static void getAnswer(double[][] lArr){    
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 18; j++) {
                System.out.printf("%.3f\t ", lArr[i][j]);
            }
            System.out.println(); // переход на новую строку после вывода 18-ти элементов одной матрицы 
        }
 }   
}