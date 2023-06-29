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

    @Test
    public void testBye() {
        GreetingService greetingService = new GreetingService();
        String name = "Alice";
        String expectedResponse = "bye Alice";

        String response = greetingService.bye(name);

        assertEquals(expectedResponse, response);
    }

    @Test
    public void testHello() {
        GreetingService greetingService = new GreetingService();
        String name = "Alice";
        String expectedResponse = "bye Alice";

        String response = greetingService.hello(name);

        assertEquals(expectedResponse, response);
    }
}
