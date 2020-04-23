<p align="center">
  <img src="src/fakerdata.ico" />
</p>

# Keypirinha Plugin: FakerData
This is FakerData, a plugin for the
[Keypirinha](http://keypirinha.com) launcher.

This plugin allows you to generate different types of fake data.

![Demo](usage.gif)

## Download
https://github.com/Fuhrmann/keypirinha-faker-data/releases


## Install
#### Managed

[@ueffel](https://github.com/ueffel) wrote [PackageControl](https://github.com/ueffel/Keypirinha-PackageControl), a package manager that eases the install of third-party packages.
It must be installed manually.

#### Manual
Once the `Fakerdata.keypirinha-package` file is installed,
move it to the `InstalledPackage` folder located at:

* `Keypirinha\portable\Profile\InstalledPackages` in **Portable mode**
* **Or** `%APPDATA%\Keypirinha\InstalledPackages` in **Installed mode** (the
  final path would look like
  `C:\Users\%USERNAME%\AppData\Roaming\Keypirinha\InstalledPackages`)


## Usage
Open Keypirinha and type 'faker'. Once the suggestions appears you can hit ENTER to generate a new fake data or TAB to list a default ammount of generated data (configurable).

## Configuration

```
# The ammount of suggestions to generate after the user selected the faker category
max_results = 5

# The language used to generate the data
# See https://faker.readthedocs.io/en/latest/#localization for all suported languages
language = en_US
```


## Change Log
### v1.0.1
* Add the required library `six`

### v1.0
* Released

## License
This package is distributed under the terms of the MIT license.


## Credits
The icon used in this plugin was provided by [icons8](https://icons8.com)

[@joke2k](https://github.com/joke2k), the developer of [faker](https://github.com/joke2k/faker) for python