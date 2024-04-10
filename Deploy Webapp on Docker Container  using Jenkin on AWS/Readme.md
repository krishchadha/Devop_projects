# Deploy Webapp on a Docker Container using Jenkins on AWS
![diagram-export-04-04-2024-10_37_27](https://github.com/krishchadha/Devop_projects/assets/30497676/36f951d9-9267-4296-a612-8e9a181dbd15)

## Agenda:

- Jenkins setup
- Maven and Git configuration
- GitHub and Maven integration with Jenkins
- Configure Docker Host
- Incorporate Jenkins with Docker
- Use Jenkins to automate the Build as well as the deployment procedure.
- Test the implementation

## Setup
Launch an instance using EC2, Aws Linux 2, free tier storage and compute
![Screenshot 2024-04-05 093755](https://github.com/krishchadha/Devop_projects/assets/30497676/5455e8ff-7941-4348-ae08-7271a3214698)
![Screenshot 2024-04-05 093920](https://github.com/krishchadha/Devop_projects/assets/30497676/c12e368f-eccf-46d5-8f04-5e9380c85271)
![Screenshot 2024-04-05 094150](https://github.com/krishchadha/Devop_projects/assets/30497676/7837e264-47a0-41b8-8366-9b73eabc36ce)
![Screenshot 2024-04-05 094218](https://github.com/krishchadha/Devop_projects/assets/30497676/8efc4510-f449-457a-8c8b-8cefa22fc8ae)
![Screenshot 2024-04-05 094523](https://github.com/krishchadha/Devop_projects/assets/30497676/ba272738-c8ae-4222-8375-0a42f5bc6d7a)
![Screenshot 2024-04-06 154100](https://github.com/krishchadha/Devop_projects/assets/30497676/f6368e12-3836-4b87-873f-4b78f5dccdeb)


Open port 8080, 22 for inbound access
![Screenshot 2024-04-05 094532](https://github.com/krishchadha/Devop_projects/assets/30497676/5bf8645f-ce67-466c-92e2-0649b4e025b9)
Launch Instance
![Screenshot 2024-04-05 094657](https://github.com/krishchadha/Devop_projects/assets/30497676/9a40cac2-8d5e-4b29-915d-e3d6515ddbbc)

Connect to instance using ssh

![Screenshot 2024-04-05 094729](https://github.com/krishchadha/Devop_projects/assets/30497676/9e8a5323-626c-4c9a-87b1-501eddecd67e)

![Screenshot 2024-04-05 095439](https://github.com/krishchadha/Devop_projects/assets/30497676/4f4f37a4-25cd-4093-b5dc-617e44e0d705)

Install Jenkins
![Screenshot 2024-04-05 095539](https://github.com/krishchadha/Devop_projects/assets/30497676/eb03d2f0-b4da-48cb-b005-33f1a351ea6e)

Install epel
![Screenshot 2024-04-06 154344](https://github.com/krishchadha/Devop_projects/assets/30497676/1f32d923-bfb1-4933-98ba-d96e43095ac4)

Install Java
![Screenshot 2024-04-06 154427](https://github.com/krishchadha/Devop_projects/assets/30497676/06ca7b5a-b4e5-4c88-9a4d-e510687534dd)

![Screenshot 2024-04-06 154513](https://github.com/krishchadha/Devop_projects/assets/30497676/d2f7c800-f5e1-468a-9f54-f8290964e18f)

Install Jenkins

![Screenshot 2024-04-06 154536](https://github.com/krishchadha/Devop_projects/assets/30497676/fb1a227e-845b-4b5e-9176-97eac3d65906)

![Screenshot 2024-04-05 100436](https://github.com/krishchadha/Devop_projects/assets/30497676/406cf108-b973-4142-bfb6-782b1d665843)

![Screenshot 2024-04-05 100733](https://github.com/krishchadha/Devop_projects/assets/30497676/f0332464-8c1d-4d4a-8210-e579d01f1531)

![Screenshot 2024-04-05 100758](https://github.com/krishchadha/Devop_projects/assets/30497676/81857b05-6150-4ea6-88b0-914b9de92dc5)

![Screenshot 2024-04-05 100822](https://github.com/krishchadha/Devop_projects/assets/30497676/6d70e06c-57d7-4cf0-a560-a65891f2bcd1)

![Screenshot 2024-04-05 100835](https://github.com/krishchadha/Devop_projects/assets/30497676/437986eb-a390-4a06-845f-8ca8af8e6967)

![Screenshot 2024-04-05 100926](https://github.com/krishchadha/Devop_projects/assets/30497676/76e66a26-3f8b-4c6e-b7c6-fb8baf7365f1)

![Screenshot 2024-04-05 101006](https://github.com/krishchadha/Devop_projects/assets/30497676/289b691b-b4af-43ce-b2b2-7563f8773337)

![Screenshot 2024-04-05 101033](https://github.com/krishchadha/Devop_projects/assets/30497676/fa7ccd6a-8b80-4499-b19d-17405192cd6f)

Install Git

![Screenshot 2024-04-05 101133](https://github.com/krishchadha/Devop_projects/assets/30497676/d7dd3d03-6fc4-4aa8-b0bd-dc19690be9e7)

![Screenshot 2024-04-05 101154](https://github.com/krishchadha/Devop_projects/assets/30497676/a5321ccc-0e89-475b-8f74-4df96cf27498)

Setup Jenkins

![Screenshot 2024-04-06 134623](https://github.com/krishchadha/Devop_projects/assets/30497676/c86ba793-3809-4ea5-9b98-f734e4b435bd)

![Screenshot 2024-04-06 134641](https://github.com/krishchadha/Devop_projects/assets/30497676/79918c0c-e0a3-4392-bc0c-a00682152161)

![Screenshot 2024-04-06 134809](https://github.com/krishchadha/Devop_projects/assets/30497676/0b3f24a8-ef88-47c5-8fb3-fe0d571afcab)


![Screenshot 2024-04-06 134825](https://github.com/krishchadha/Devop_projects/assets/30497676/648b6b95-74a4-4e52-b4cb-7b9574264027)

![Screenshot 2024-04-06 134857](https://github.com/krishchadha/Devop_projects/assets/30497676/18c9fbb8-42b8-4e75-bd87-e3461f1cc812)

![Screenshot 2024-04-06 134914](https://github.com/krishchadha/Devop_projects/assets/30497676/45fab116-4a47-4d49-bab7-6b5f95e7a329)

Install Maven

![Screenshot 2024-04-06 140714](https://github.com/krishchadha/Devop_projects/assets/30497676/22c1ac5b-0dc1-498b-81ae-1a11e162e683)

![Screenshot 2024-04-06 141101](https://github.com/krishchadha/Devop_projects/assets/30497676/c6a86255-79f0-497d-8ed2-b2af11781760)

![Screenshot 2024-04-06 141743](https://github.com/krishchadha/Devop_projects/assets/30497676/133ab609-3c5f-492e-8861-de7974b475de)

![Screenshot 2024-04-06 141906](https://github.com/krishchadha/Devop_projects/assets/30497676/2b0c3fd4-210a-4e2a-9445-7ae36a400da9)

![Screenshot 2024-04-06 141951](https://github.com/krishchadha/Devop_projects/assets/30497676/4fe0f219-0c1c-4e66-9858-bfe567249b16)

![Screenshot 2024-04-06 145506](https://github.com/krishchadha/Devop_projects/assets/30497676/34690481-b378-4602-a383-22dd29eb6836)

![Screenshot 2024-04-06 164000](https://github.com/krishchadha/Devop_projects/assets/30497676/ed281379-58bc-4d56-82fe-a61b45c955a5)

Install Docker

![Screenshot 2024-04-06 164434](https://github.com/krishchadha/Devop_projects/assets/30497676/1e70a689-4685-4ab5-8623-551b8a1e5934)

![Screenshot 2024-04-06 164434](https://github.com/krishchadha/Devop_projects/assets/30497676/db5a3929-9d21-4456-bb5b-59ad6827bd0b)

![Screenshot 2024-04-06 164553](https://github.com/krishchadha/Devop_projects/assets/30497676/628acec3-6fd1-491a-af34-89b570e1e4a9)

![Screenshot 2024-04-06 164634](https://github.com/krishchadha/Devop_projects/assets/30497676/04c869d3-ff3b-406f-b3df-13ae2d7b2112)

![Screenshot 2024-04-06 164822](https://github.com/krishchadha/Devop_projects/assets/30497676/408a8947-9408-4185-bc97-34dcb3e192a6)

Visit Tomcat Website

![Screenshot 2024-04-06 165035](https://github.com/krishchadha/Devop_projects/assets/30497676/383ae612-739f-499c-a7c5-b956c05e56d1)

Make a Dcokerfile

![Screenshot 2024-04-06 165646](https://github.com/krishchadha/Devop_projects/assets/30497676/5ff6941d-e876-4bbd-893b-4edd2354101f)

![Screenshot 2024-04-06 165722](https://github.com/krishchadha/Devop_projects/assets/30497676/5691648b-b7ac-48b0-a699-eee018e3e067)

![Screenshot 2024-04-06 165744](https://github.com/krishchadha/Devop_projects/assets/30497676/14828603-7268-4f5f-8318-80d1a28f8f85)

![Screenshot 2024-04-06 165806](https://github.com/krishchadha/Devop_projects/assets/30497676/5ff5b908-01ea-4388-9413-8aaed9c208b0)

![Screenshot 2024-04-06 165827](https://github.com/krishchadha/Devop_projects/assets/30497676/c6cf4913-31fc-4a13-8706-4cc57c46a0b9)

![Screenshot 2024-04-06 165946](https://github.com/krishchadha/Devop_projects/assets/30497676/2c1dce9c-c11e-4cca-95a3-a37f6e40d070)

![Screenshot 2024-04-06 170049](https://github.com/krishchadha/Devop_projects/assets/30497676/3d34e4d5-9f53-4c31-8d6a-ea9211e81120)

![Screenshot 2024-04-06 170130](https://github.com/krishchadha/Devop_projects/assets/30497676/6c3145f1-a217-4f6c-9efb-d97144275205)

![Screenshot 2024-04-06 170243](https://github.com/krishchadha/Devop_projects/assets/30497676/ee80d004-80fe-4920-9d5c-74fc67ee9594)

![Screenshot 2024-04-06 170327](https://github.com/krishchadha/Devop_projects/assets/30497676/06ee0c29-246a-48d1-927c-191202d8819a)

![Screenshot 2024-04-06 170429](https://github.com/krishchadha/Devop_projects/assets/30497676/f0dc7625-047b-49d0-9ce9-ea8dc8b7e3ce)

![Screenshot 2024-04-06 170652](https://github.com/krishchadha/Devop_projects/assets/30497676/681f87d3-4a86-4b4e-8b85-6635bd7b1e70)

![Screenshot 2024-04-06 170914](https://github.com/krishchadha/Devop_projects/assets/30497676/79833756-eb02-47e3-97d9-9ce00bebf3bc)

![Screenshot 2024-04-06 170944](https://github.com/krishchadha/Devop_projects/assets/30497676/b334cc26-c0f5-4141-8436-75c3ed75d3e9)

Create Project in Jenkins

![Screenshot 2024-04-07 154438](https://github.com/krishchadha/Devop_projects/assets/30497676/0d9974b3-2630-4493-9afb-850e1f213841)

![Screenshot 2024-04-07 155216](https://github.com/krishchadha/Devop_projects/assets/30497676/be0cff66-d60b-486f-aa8d-febe6ac0cbb1)

![Screenshot 2024-04-07 155258](https://github.com/krishchadha/Devop_projects/assets/30497676/f79aa063-776c-47e0-90bd-e8045d18aded)

![Screenshot 2024-04-07 160014](https://github.com/krishchadha/Devop_projects/assets/30497676/1d610400-344c-47d6-8a61-155e6cb1fd74)
  
![Screenshot 2024-04-07 160350](https://github.com/krishchadha/Devop_projects/assets/30497676/fe66c6fe-6210-4573-868e-e3fd4b036ec1)

![Screenshot 2024-04-07 160641](https://github.com/krishchadha/Devop_projects/assets/30497676/c4089687-1ebb-4939-a8c3-be52bedf0433)

![Screenshot 2024-04-07 163240](https://github.com/krishchadha/Devop_projects/assets/30497676/268cf06c-dda2-411f-8847-7ea31828547d)

![Screenshot 2024-04-10 190008](https://github.com/krishchadha/Devop_projects/assets/30497676/0e8f6567-35c7-478a-aa46-d28b89aeb117)

























