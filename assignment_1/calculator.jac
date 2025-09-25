# calculator.jac

walker perform_calculation {
    has a: int;
    has b: int;
    has op: str;

    can "calculate" with `root entry {
        result = 0.0;
        if op == "+" {
            result = a + b;
        } elif op == "-" {
            result = a - b;
        } elif op == "*" {
            result = a * b;
        } elif op == "/" {
            if b != 0 {
                result = a / b;
            } else {
                std.out("Error: Division by zero");
                result = -1.0;
            }
        } else {
            std.out("Error: Invalid operator");
            result = -1.0;
        }
        std.out(result);
    }
}

with entry {
    spawn `root walker::perform_calculation(a=10, b=5, op="*");
}