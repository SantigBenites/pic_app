#[macro_use] extern crate rocket;
use std::sync::Mutex;

#[derive(Default)]
struct Counter {
    value: Mutex<i64>
}

#[get("/")]
fn index() -> &'static str {
    "Hello, world!"
}


#[get("/counter")]
fn counter(state: &rocket::State<Counter>) -> String {
    let x = state.value.lock().unwrap();
    format!("Counter is {}", *x)
}



#[get("/counter_add")]
fn counter_add(state: &rocket::State<Counter>) -> String {
    let mut x = state.value.lock().unwrap();
    *x += 1;
    format!("Counter incremented to {}", *x)
}



#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(Counter { value: Mutex::new(1) })
        .mount("/", routes![index, counter, counter_add])
}