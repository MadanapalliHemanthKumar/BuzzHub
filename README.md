## BuzzHub

Simple multiplayer buzzer system.

[BuzzHub.App](https://web.abhimanyurajeesh.buzz/)
(The web App is locally hosted so might not be available all the time.)

### Development

- Prerequisites: node and a package manager (e.g. npm, yarn)
- Run `yarn install` to install dependencies
- Run `yarn dev` to run local client on localhost:4000 and local server on localhost:4001

### Deployment

- Build React app using `yarn build`
- Run `yarn start` to run the Koa server, which will serve the built React app (via '/build'), as well as operate both the boardgame.io server and lobby
