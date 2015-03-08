# Darwin

A general non-binary, paralelized genetic algorithm framework

## Installation

TODO: Describe the installation process

## Usage

### Implement an Individual Class
Create an object inheriting from Individual, implementing the mutate and survival_test functions. 

The genes of the individual are stored in genetic_code list, keeping their order throughout evolution.

### Instanciate a world
Instanciate a world providing one or more initial individuals (adam).
If provided with one individul, random mutations of the individual will populate the world

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

