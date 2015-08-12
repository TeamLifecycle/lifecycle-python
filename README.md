# lifecycle-python
## Visit lifecycle.io for further documentation and customer service contact information

#### [Lifecycle](http://www.lifecycle.io) official python library

## Installation
```
pip install lifecycle==3.7.2
```
Examples and instructions for the SDK are available in their acompanying README.md, migration.md and examples directories under their specific platform directories:

<!-- [Standalone Python - Everyday python for your scripts and apps](python)

[Tornado - For use with the Python Tornado Framework](python-tornado)

[Twisted - For use with the Python Twisted Framework](python-twisted) -->

```python
import 'lifecycle_api'
```

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install lifecycle_api

## Usage
To use, simply create an instance of the client and identify and track away!

```python
require 'lifecycle_api'

lifecycle = Lifecycle::Client.new 'YOUR_LIFECYCLE_API_KEY'
```

TO IDENTIFY:
```ruby
lifecycle.identify params #(see example of params)
```

TO TRACK:
```ruby
lifecycle.track 'event_id', 'unique_id'
```


```python
#Example of params variable to use with identify call
#NOTICE: .to_json at the end. The api will not be able
#to parse your request without this.
params = {:unique_id => "1234",
          :first_name => "Nathan",
          :last_name => "Mooney",
          :email_address => "someone@getvenn.io",
          :phone_number => "12345678913"
}.to_json
```

Use this library to interact with your Lifecycle account. Easily identify users and track users with minimal code. If you are looking for packages in a language other than ruby, check out the TeamLifecycle organization for your desired language. It is our hope that by providing this library, integration and usage of Lifecycle will be quick and easy.

```
pip install lifecycle
```

## Contact support@pubnub.com for all questions
