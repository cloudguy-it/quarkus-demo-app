package org.acme.testcoverage;

import javax.enterprise.context.ApplicationScoped;

@ApplicationScoped
public class GreetingService {

    public String greeting(String name) {
        return "hello " + name;
    }

    public String bye(String name) {
        return "bye " + name;
    }

}