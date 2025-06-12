#[macro_use] extern crate rocket;

#[get("/")]
fn index() -> &'static str {
    "Hello, world!"
}


#[get("/counter")]
fn counter() -> int64 {
    f"Hello {}"
}



#[get("/counter_add")]
fn counter_add() -> void{
    x = x+ 1;
}


#[launch]
fn rocket() -> _ {
    let mut x = 1
    rocket::build().mount("/", routes![index])
                    .mount("/counter", routes![counter])
                    .mount("/counter_add", routes![counter_add])
}
