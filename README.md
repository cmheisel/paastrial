h1. cmheisel's paas trial

I chose to deploy [twitter-dedpue](http://github.com/cmheisel/twitter-dedupe) to Heroku to power [@slatemaglite](https://twitter.com/slatemaglite).

For fun, I'm writing a series of [blog posts](http://chrisheisel.com) breaking out what it takes to deploy this app to a variety of [Platforms as a service](http://en.wikipedia.org/wiki/Platform_as_a_service). I intend to keep my (sanitized) config files here and probably some raw notes of what it took to get things set up.

For each service, my goal is to:
1. Provision redis
2. Deploy daemon
3. Access logs
4. Do it all again for a staging environment

I'll be trying out these services:
1. [Heroku](http://www.heroku.com)
2. [Dotcloud/Cloudcontrol](https://www.dotcloud.com/)
3. [Elastic Beanstalk](http://aws.amazon.com/elasticbeanstalk/)
4. [Gondor.io](https://gondor.io/)
5. [Google Compute Engine](https://cloud.google.com/compute/)
5. Anything else someone recommends to me :-)
