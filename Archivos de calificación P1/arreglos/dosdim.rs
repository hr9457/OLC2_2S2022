fn llenarMat(a: [[i64; 3]; 3], b:[[i64; 3]; 3]) {
    for i in 0..a.len() {
        for j in 0..a.len() {
            a[i][j] = (j as i64) * 3 + (i as i64);
            b[i][j] = i64::pow((i as i64), 3) - i64::pow((j as i64), 2);
        }
    }
}

fn sumarMat(a: [[i64; 3]; 3], b: [[i64; 3]; 3], r:  [[i64; 3]; 3]) {
    for i in 0..3 {
        for j in 0..3 {
            r[i][j] = (a[i][j]) + (b[i][j]);
        }
    }
}

fn restarMat(a:  [[i64; 3]; 3], b:  [[i64; 3]; 3], r:  [[i64; 3]; 3]) {
    for i in 0..3 {
        for j in 0..3 {
            r[i][j] = (a[i][j]) - (b[i][j]);
        }
    }
}

fn multMat(a:  [[i64; 3]; 3], b:  [[i64; 3]; 3], r:  [[i64; 3]; 3]) {
    for i in 0..3 {
        for j in 0..3 {
            for k in 0..3 {
                r[i][j] = (r[i][j]) + (a[i][k]) * (b[k][j]);
            }
        }
    }
}

fn limpiarMat(a:  [[i64; 3]; 3]) {
    for i in 0..3 {
        for j in 0..3 {
            a[i][j] = 0;
        }
    }
}

fn printMat(r:  [[i64; 3]; 3]) {
    for i in 0..r.len() {
        println!("{}", r[i]);
    }
}

fn main() {
    let mut matA: [[i64; 3]; 3] = [[0,0,0],[0,0,0],[0,0,0]];
    let mut matB: [[i64; 3]; 3] = [[0,0,0],[0,0,0],[0,0,0]];
    let mut matR: [[i64; 3]; 3] = [[0,0,0],[0,0,0],[0,0,0]];

    // /* llenar matriz */
    llenarMat(matA, matB);

    println!("Matriz A");
    printMat(matA);
    println!("");
    println!("Matriz B");
    printMat(matB);
    println!("");
    println!("Matriz R");
    printMat(matR);
    println!("");

    // sumar matriz
    sumarMat(matA, matB, matR);
    println!("R = A + B");
    printMat(matR);
    println!("");

    // /* restar matriz */
    limpiarMat(matR);
    restarMat(matA,matB, matR);
    println!("R = A - B");
    printMat(matR);
    println!("");

    // /* multiplicar matriz */
    limpiarMat(matR);
    multMat(matA, matB, matR);
    println!("R = A * B");
    printMat(matR);
    println!("");
}


// /*
// Matriz A
// [0, 3, 6]
// [1, 4, 7]
// [2, 5, 8]

// Matriz B
// [0, -1, -4]
// [1, 0, -3]
// [8, 7, 4]

// Matriz R
// [0, 0, 0]
// [0, 0, 0]
// [0, 0, 0]

// R = A + B
// [0, 2, 2]
// [2, 4, 4]
// [10, 12, 12]

// R = A - B
// [0, 4, 10]
// [0, 4, 10]
// [-6, -2, 4]

// R = A * B
// [51, 42, 15]
// [60, 48, 12]
// [69, 54, 9]
// */