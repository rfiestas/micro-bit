let temperature_tmp = 0
let hot_mode = false

basic.forever(function () {
    // Use A button to print degrees.
    // Use B button to switch hot mode.
    // Hot mode off, each point is 1 degree.
    // Hot mode on, each point ara 2 degrees.
    let temperature = input.temperature()
    if (input.buttonIsPressed(Button.A)) {
        basic.clearScreen()
        basic.showString(temperature.toString(), 300)
        draw(temperature)
    }
    if (input.buttonIsPressed(Button.B)) {
        hot_mode = !hot_mode
        basic.clearScreen()
        if (hot_mode) {
            basic.showString('on', 300)
        } else {
            basic.showString('off', 300)
        }
        draw(temperature)
    }
    if (temperature != temperature_tmp) {
        draw(temperature)
        temperature_tmp = temperature
    }
})
function draw(temperature: number) {
    // draw, draw temperature on screen
    let counter = 1
    let inc = 1
    let modification = 0
    let max_counter = Math.abs(temperature)
    if (temperature <= 0) {
        modification = 4
    }
    if (hot_mode && temperature >= 0) {
        inc = 2
    }
    basic.clearScreen()
    for (let x = 0; x < 5; x++) {
        for (let y = 4; y > -1; y--) {
            led.plot(modification + x, y)
            counter += inc
            if (counter > max_counter) {
                break
            }
        }
        if (counter > max_counter) {
            break
        }
    }
}
