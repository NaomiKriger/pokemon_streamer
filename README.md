# Pokemon Streamer

![img_1.png](pics/ash_and_pokemons.png)

## HELLO THERE ASH KETCHUM AND WELCOME TO THE POKEMON STREAMER!

I hope you're ready to start streaming Pokemons, because it's time to catch 'em all!
So, how are we gonna make this work?


# About the App
This is an app that is meant to consume streams of `Pokemons`, 
where a `Pokemon` is a message body encoded in Protobuf protocol. 
An example of a not-encoded `Pokemon` can be found 
[here](tests/samples_for_local_e2e/pokemon_not_protobuf.json).

Once a `Pokemon` is consumed by the `stream` endpoint, it is normalized and routed 
to a relevant endpoint, according to a pre-configured list of rules.
An example for such list of rules can be found [here](rules_config.json).

The Protobuf schema that the messages are decoded based on, can be found 
[here](pokedex/pokedex.proto) .

## Flow
1. The user sends a `POST` request to a streamer (see [Tests](#Tests) section for more info), with a request signature in the request's header.
2. A `Pokemon` (or a stream of `Pokemons`) is sent to `/stream` endpoint
3. The incoming message's request signature is validated, and then the request body is parsed
4. The request's body is matched against a list of rules provided in the config file
5. If a rule is matched, the request is formatted to JSON and forwarded to the rule's destination. JSON should be an accurate representation of the protobuf schema (preserve naming conventions and types)
6. The destination's response is sent to the `Pokemon`'s sender



# Run App Locally

* Start the server
* Send a request to the `/stream` endpoint. The request's components should include:
    * A header named `Is-Local-Test` with a value set to `true`
    * A header named `X-Grd-Signature`

## Tests
* Two test samples are provided in `tests/samples_for_local_e2e` - a happy flow scenario, and a non-protobuf Pokemon.
    * The corresponding parameters which were provided for the `happy_flow` Pokemon are:
        * `ENCRYPTION_SECRET` = `lpk5rO7xeG9df9IgBbt48zdnQLEHFJ3e4YpxZbElPR0=`
        * `X-Grd-Signature` = `78ff9405af88176eaf5ad70d195d9e2f778ef6de8bba78039f82735d5529c38a`


# Run App In Prod

Running the app in prod requires deploying the app to a public cloud provider. 
I deployed the app to Heroku, and I scale up a dyno when I want to use the app.
There's a streamer which streams Pokemons upon `POST` requests to a publicly available API (`/stream` endpoint), 
but it is currently unavailable. You can create your own such streamer if you want to try it out.

---

## Wishing you a day full of Pikachus 🙂

![img.png](pics/pikachu_hi__in_nature.png)
