for f in *.fas
do chai-lab fold --use-templates-server --use-msa-server $f ${f%.fas}
done
