package org.acme.testcoverage;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class GreetingServiceTest {

    @Test
    public void testGreeting() {
        GreetingService greetingService = new GreetingService();
        String name = "Alice";
        String expectedResponse = "hello Alice";

        String response = greetingService.greeting(name);

        assertEquals(expectedResponse, response);
    }
}
