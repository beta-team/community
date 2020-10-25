# Beta Project Notes  (2020.10.25)

> 2020.10.25
>
> By Siwei Liu	Email: siweiliu525@gmail.com
>
> Chair: Siwei Liu
>
> Next Chair: Zaiqiao Meng

------
### Attendees:

Zaiqiao Meng (UoC)

Xi Wang (UoG)

Siwei Liu (UoG)

Yucheng Liang (SYSU)

Shuqi Mo (SYSU)

Langning Liang (SYSU)

## Discuss

1. n_test in the *data split* does not match its functionality, which should be referred as *num_test_set*. 
2. Documentation of the class of *Dataset*.
3. Merge Commnits before PR: it's better to use One commit for each issue.

Formating:

 ```shell
flake8==3.7.9
flake8-black==0.2.1
flake8-isort==4.0.0
flake8-docstrings==1.5.0
flake8-nb
isort==5.5.2
 ```




## TODOs

- [ ] Merge the current develop branch to the master branch and release another version of Beta-RecSys.
- [ ] Update models with new interface. (LightGCN and NCF) (**Siwei**)
- [ ] Check models and benchmarking. 
- [ ] Docker image for the project and maintain it. (**Bingchang**)

- [ ] Add pip description (**Xi**)

- [ ] Try all available models and check ambigous descriptions 

- [ ] Update Ray along with the issue page (**Zaiqiao, Siwei**)

  

### Meeting

Regular Time: (bi-weekly) week day or weekend?  8 hour time lag.

https://doodle.com/poll/avp5uxv9yxg8axc9

Permanent link: Team

>Join on your computer or mobile app with the following link:

>[Click here to join the meeting](https://teams.microsoft.com/l/meetup-join/19%3ameeting_N2NjNTY0YmItODMwYy00ZWJkLTliNjEtZGU0MDQ2NTU5OWI1%40thread.v2/0?context={"Tid"%3a"49a50445-bdfa-4b79-ade3-547b4f3986e9"%2c"Oid"%3a"9a357428-3b38-4bb3-b51f-841331c84c0b"})

Meeting Recording: Youtube:https://www.youtube.com/playlist?list=PLB41jgIt5eOsztNk9iPa9QktkZq6DksMV  

Meeting Hosting and Note Taking:

		- Add Attendees in meeting notes.
		- Release Agenda two days before the meeting.
		- Agenda (Recommended & Can be improved.):

* * Review Current Issues

    > Summarise current progress

  * Review Documentation 

    > This should be review for each meeting. Improving Documentation is more important than improving a feature.

  * Review Milestone

    > Make sure that we are still on the right direction.

  >New version release

  * New Issues for the Next Step

  * Presentation for a specific model. E.g. Introduce SASrec model, and review their codes and discuss about the implementation under Beta-recsys

    

### Dissemination 

Twitter Account/ Weibo: 

Blog & personal pages: 

Mailing List: Xi Wang

Slack: Zaiqiao Meng

Zhihu: 

StackOverflow:



Some good examples:

- https://github.com/oam-dev/spec
- https://github.com/rusty1s/pytorch_geometric
- https://github.com/ray-project/ray



