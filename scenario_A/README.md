
# Scenario A

## Context 

A startup (but not limited to startups) wants to train AI models on the platform (TeraLab Marketplace). They bring their own datasets (~100 GB), they would like to compare with existing datasets from the platform. They would need algorithms as well as an autonomous workspace.


_Unless explicitly stated, the datasets referred to are less than 100 GB. This is a magnitude compatible with SFTP and SCP technologies. Users need to pay attention._


## Prerequisites

* [Create an Autonomous Workspace]()
* Expose an SSH port forwarding in the autonomous workspace
* [Deploy an instance of TeraLab Marketplace]() inside the created Workspace with access restricted to the workspace users

## Instructions

### Variables

* workspace_id : ID of the workspace (example : ws67) after first prerequisite is fulfilled
* username : username of the user account deployed on the workspace after first prerequisite is fulfilled
* ssh_wan_port 
* local_path_to_data : example /path/local/data

### Manual:

* [Add resources to your Marketplace instance]()
* Upload your data on in the workspace (< 100 GB to transfer on TeraLab)

```bash
scp -r ${ local_path_to_data} -p ${ssh_wan_port} ${username}@${workspace_id}.tl.teralab-datascience.fr/home/${username}
```

* Connect to the workspace

```bash
ssh -p ${ssh_wan_port}  ${username}@${workspace_id}.tl.teralab-datascience.fr
```

* [Configure an NFS endpoint to your data]()
* [Create a Workshop Storage using the NFS specifications]()
* [Create a workshop App using the storage just created]() 

## Outcome (Validation Condition):

* An autonomous workspace ${workspace_id} containing : 
  * A TeraLab Marketplace instance with some resources : 
* Apps to process user’s data
* Data for user to compare his results with
  * The user’s Data imported via SCP
  * The Data made available using an NFS type workshop storage
  * Data  processed using App instances. 
