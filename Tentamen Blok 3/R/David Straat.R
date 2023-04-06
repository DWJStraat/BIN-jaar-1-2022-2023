# Set up library
library(package="MASS")

# First Dataset

?survey
summary(survey)

# 1
Height <- survey$Height
Wr.Hnd <- survey$Wr.Hnd

plot(Height, Wr.Hnd, main = "Height vs Wr.Hnd", xlab = "Height", ylab = "Wr.Hnd", sub = "David Straat")

# 2

Height <- survey$Height
Wr.Hnd <- survey$Wr.Hnd
Female_Height <- survey$Height[survey$Sex == "Female"]
Female_Wr.Hand <- survey$Wr.Hnd[survey$Sex == "Female"]


plot(Height, Wr.Hnd, main = "Height vs Wr.Hnd", xlab = "Height", ylab = "Wr.Hnd", sub = "David Straat")
points(Female_Height, Female_Wr.Hand, col = "red", pch = 19)

# 3

Height <- survey$Height
Wr.Hnd <- survey$Wr.Hnd
Female_Height <- survey$Height[survey$Sex == "Female"]
Female_Wr.Hand <- survey$Wr.Hnd[survey$Sex == "Female"]
Male_Height <- survey$Height[survey$Sex == "Male"]
Male_Wr.Hand <- survey$Wr.Hnd[survey$Sex == "Male"]

plot(Height, Wr.Hnd, main = "Height vs Wr.Hnd", xlab = "Height", ylab = "Wr.Hnd", sub = "David Straat")
points(Female_Height, Female_Wr.Hand, col = "red", pch = 19)
points(Male_Height, Male_Wr.Hand, col = "blue", pch = 19)
legend("topleft", legend = c("Female","Male", "Unknown"), col = c("red","blue", "black"), pch = c(19,19,1))

# 4
Pulse <- survey$Pulse
Smoke <- survey$Smoke
Smoke <- factor(Smoke, c("Never", "Occas", "Regul", "Heavy"))
boxplot(Pulse ~ Smoke, main = "Pulse compared to smoking frequency", xlab = "Smoke", ylab = "Pulse", sub = "David Straat")

# New Dataset

summary(Melanoma)
?Melanoma

# 5 a
thickness <- Melanoma$thickness
thickness_alive <- thickness[Melanoma$status == 2]
thickness_dead <- thickness[Melanoma$status == 1]
summary(thickness_alive)
summary(thickness_dead)

# 5 b
age <- Melanoma$age
hist(age, main = "David Straat", xlab = "Age")

# 6
age <- Melanoma$age
hist(age, main = "David Straat", xlab = "Age")
first_quarter <- quantile(age, 0.25)
abline(v = first_quarter, col = "red", lwd = 2)

# 7
ulcer <- Melanoma$ulcer
sex <- Melanoma$sex
chisq.test(ulcer, sex)

# 9
ulcer <- Melanoma$ulcer
sex <- Melanoma$sex
chisq.test(ulcer, sex)$p.value < (1 - 0.95)