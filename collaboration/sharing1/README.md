
# Collaboration through TeraLab Marketplace: Sharing resources (A1 & D1) to be used for the project

## Pre-requisites

* Familiarity with the Marketplace (read the workflow [Getting Started with TeraLab Marketplace]() to get introduced)

## Instructions

### Variables

### Manual

* as developer A:
  * Login on the Marketplace
  * In the navigation, click on "Home"
  * In hte "Marketplace" section, click on the button "You can contribute here"
  * Follow instructions to create App (Type field of the form should be Docker Container)
  * When redirected to the (newly created) resource's page, look for the "Download" collapse all the way to the bottom of the page and click on the "red feather" to change the resource's archive (FYI: that is the actual archive downloaded when users attempt to download your resource).
  * Clicking the red feather opens a form, provide a <code>*.zip</code> file (containing a docker-compose.yaml since the resource's type is "Docker Container")
* as developer B:
  * Follow the same steps as developer A with just the following differences:
    * Resource Type is Dataset
    * archive file contains a <code>*.csv</code> file instead of a <code>docker-compose.yaml</code>.
* coming soon: videos showing how to practically make these operations


## Outcome

* sharing the resources of developers A (A1) and B (D1) on the Marketplace