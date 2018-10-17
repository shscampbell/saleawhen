# Sale A-When?
## Predicting the time to sell your home in the Calgary, Alberta, Canada market. Receive data-based forecasts of days-on-market for your Calgary listing at <a href="http://saleawhen.site/">http://saleawhen.site/</a>

This is the source code for a webapp I created as an <a href="http://www.insightdatascience.com/">Insight Data Science Fellow</a>. This was part of a consulting project for a Canadian real-estate startup. The company was interested in creating a model that could predict how long a listed house would take to sell. They provided a proprietary data set of over 50 000 sold homes since 2010, including detailed information about each property and their neighborhoods. That data resulted in the predictive model used by Sale A-When.

The webapp is a webform that queries users for relevant details about their listing and for the level of confidence that they want to have about how long it will take their property to sell. For example, if the user selects a confidence level of 99, the resulting output would be the number of days required for 99% of similar listings to sell.

## Motivation
An accurate prediction of the number of days expected for a home to sell is valuable information for anyone planning to sell their home. It helps sellers make appropriate moving plans and it helps them pinpoint the best time to put their property on the market.

This information is also important to property investors who need to understand the liquidity of their assets. Home flippers who buy properties to upgrade and re-sell them at a profit need to estimate how much holding costs will eat into their profit margins, such as mortgage interest, property insurance, and maintenance.

Sale A-When provides information about how different upgrades to a property could impact the days-on-market. Information about the full days-on-market distribution is also provided so that sellers can make appropriate contingency plans for every eventuality.

## Screenshot

<img src="saleawhen_screenshot.png" />

## Tech/framework used

<b>Built with</b>
- [Python](https://www.python.org/)
- [Flask](https://flask.pocoo.org/)

## License
GNU General Public License v3

GNU © [Sheldon Campbell](https://www.github.com/shscampbell/)