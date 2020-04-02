pour creer le repertoire grp-5-maint en local(à faire qu'une fois au début):


Admettons que vous vous situez dans /Chemin

git clone https://github.com/MaximeLafont/grp-5-maint

A chaque fois que vous voulez modifier le code il faut que vous regardiez en amont ce qui a été modifié depuis votre dernière arrivé. Si vous ne voulez pas télécharger les dernières modification, ne faites rien, sinon faites:

cd /Chemin/grp-5-main

git pull

Cela va automatiquement vous rajouter toutes les modification faites.

Ensuite, modifiez ce que vous voulez.
Pour uploader les nouvelles modification que vous avez fait:

cd /chemin/grp-5-maint

si vous voulez uploader les modifications faites sur tous les fichier de notre projet:

git add . 

si vous voulez uploader les modifications d'un seul fichier en particulier, faites:

cd cheminVersVotreFichier

git add fichier

Ainsi de suite

Ensuite:

git commit -m "quelles ont été vos midifications"

git push

Dans tous les cas, même si vous n'êtes pas sure de vos commit, on a accès à tous les commit d'avant donc n'hésitez pas à pusher.

