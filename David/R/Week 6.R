lungcap <- read.table("David/R/Longcapaciteit.txt", header = T, sep = "\t")
attach(lungcap)
head(lungcap)
plot(LungCap ~ Age)
plot(LungCap[Gender=="female"]~Age[Gender=="female"], ylim = c(0,15), xlim=c(0,20), main="Longcapaciteit tegen leeftijd", col=2, pch=3, xlab ="Age", ylab="Lungcap")
points(LungCap[Gender=="male"]~Age[Gender=="male"], ylim = c(0,15), xlim=c(0,20), main="Longcapaciteit tegen leeftijd", col=4, pch=4, xlab ="Age", ylab="Lungcap", cex = 0.5)
abline(lm(LungCap[Gender == "male"] ~ Age[Gender == "male"]), col = 4)
abline(lm(LungCap[Gender == "female"] ~ Age[Gender == "female"]), col = 2)
legend("topleft", legend = c("female", "male"), col = c(2, 4), pch = c(3,4))

cor(LungCap, Age)
cor.test(LungCap, Age)

pairs(lungcap[,1:3])

?airquality

head(airquality)
cor.test(Wind, Ozone)

chisq.test(Smoke, Caesarean)

plot(Height ~ LungCap, col = 1, xlab = "LungCap", ylab = "Height")
plot(Height[Smoke == "yes"] ~ LungCap[Smoke == "yes"],col = 3, xlab = "LungCap", ylab = "Height")
abline(lm(Height[Smoke == "yes"] ~ LungCap[Smoke == "yes"]), col = 3)
points(Height[Smoke == "no"] ~ LungCap[Smoke == "no"],col = 2)
abline(lm(Height[Smoke == "no"] ~ LungCap[Smoke == "no"]), col = 2)
legend("topleft", legend = c("smokes", "doesn't smoke"), col = c(3, 2), pch = 1)