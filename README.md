# SublimeCmpilr

Sublime Text Plugin for [cmpilr](https://github.com/hiroyan/cmpilr.git]).
edited file compiled after save.

# Supported Formats

* CoffeeScript
* Haml
* Sass

## Settings

Cmpilr.sublime-settings

```json
{
  /**
   * REQUIRED
   *
   * compiler web api URL. this should be changed from default value.
   */
   "cmpilr_url" : "https://cmpilr.herokuapp.com",

   /**
    * REQUIRED
    *
    * supported formats and corresponding compiled formats
    */
  "compilers" : {
    "haml" : "html",
    "scss" : "css",
    "coffee" : "js"
  },

   /**
    *  overrwrite wihtout comfirm dialog
    */
  "force_overwrite" : true
}
```
