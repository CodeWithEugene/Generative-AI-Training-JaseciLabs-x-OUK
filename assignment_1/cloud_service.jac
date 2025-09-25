# cloud_service.jac

walker get_hello {
    can "get_hello" with `root entry;

    root {
        report "Hello from the cloud!";
    }
}
