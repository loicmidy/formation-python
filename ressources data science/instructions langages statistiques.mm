<map version="1.0.1">
<!-- To view this file, download free mind mapping software FreeMind from http://freemind.sourceforge.net -->
<node CREATED="1556957777079" ID="ID_1562233462" MODIFIED="1556957804135" TEXT="instructions langages statistiques">
<node CREATED="1556957862830" ID="ID_1334721019" MODIFIED="1556957873596" POSITION="right" TEXT="table type dataframe">
<node CREATED="1556957876123" FOLDED="true" ID="ID_119835763" MODIFIED="1556993927233" TEXT="cr&#xe9;ation dataframe &quot;&#xe0; la main&quot;">
<node CREATED="1556957891609" FOLDED="true" ID="ID_951202645" MODIFIED="1556993925848" TEXT="PYTHON PANDAS">
<node CREATED="1556958438691" ID="ID_306144397" MODIFIED="1556958440241" TEXT="notesElevesMati&#xe8;res=pd.DataFrame({&apos;math&apos;:[2,10,15,17,20,8],&apos;physique&apos;:[np.nan,9,14,12,17,17],&apos;sexe&apos;:[&apos;H&apos;,&apos;F&apos;,&apos;H&apos;,&apos;F&apos;,&apos;H&apos;,&apos;F&apos;]},index=[&apos;a&apos;,&apos;b&apos;,&apos;c&apos;,&apos;d&apos;,&apos;e&apos;,&apos;f&apos;]) "/>
</node>
<node CREATED="1556958441902" FOLDED="true" ID="ID_1730899726" MODIFIED="1556993924167" TEXT="R BASE">
<node CREATED="1556958455797" ID="ID_485975411" MODIFIED="1556958457396" TEXT="notesElevesMati&#xe8;res&lt;-data.frame(math = c(2,10,15,17,20,8),physique = c(NA,9,14,12,17,17),sexe = c(&apos;H&apos;,&apos;F&apos;,&apos;H&apos;,&apos;F&apos;,&apos;H&apos;,&apos;F&apos;)) "/>
</node>
</node>
<node CREATED="1556958354879" FOLDED="true" ID="ID_76886399" MODIFIED="1556993928770" TEXT="afficher infos &quot;de base&quot; sur dataframe">
<node CREATED="1556958371785" FOLDED="true" ID="ID_728099530" MODIFIED="1556993921449" TEXT="PYTHON PANDAS">
<node CREATED="1556958403028" ID="ID_1743004486" MODIFIED="1556958404450" TEXT="print(notesElevesMati&#xe8;res.info())"/>
<node CREATED="1556958404852" ID="ID_1775971437" MODIFIED="1556958416145" TEXT="print(notesElevesMati&#xe8;res.describe(include=&apos;all&apos;))"/>
</node>
<node CREATED="1556958376232" FOLDED="true" ID="ID_1999795977" MODIFIED="1556993922856" TEXT="R BASE">
<node CREATED="1556959073791" ID="ID_1354309764" MODIFIED="1556959075139" TEXT="str(notesElevesMati&#xe8;res) "/>
<node CREATED="1556978393685" ID="ID_1437327737" MODIFIED="1556978419842" TEXT="DPLYR glimpse(notesElevesMati&#xe8;res)"/>
<node CREATED="1556959075980" ID="ID_1858939059" MODIFIED="1556959088195" TEXT="summary(notesElevesMati&#xe8;res)"/>
</node>
</node>
<node CREATED="1556959036643" ID="ID_1317051971" MODIFIED="1556992997461" TEXT="imports">
<node CREATED="1556959041902" FOLDED="true" ID="ID_1024562136" MODIFIED="1556993929999" TEXT="CSV">
<node CREATED="1556959047155" FOLDED="true" ID="ID_869614741" MODIFIED="1556993918527" TEXT="PYTHON PANDAS">
<node CREATED="1556959055835" ID="ID_1922196362" MODIFIED="1556961503005" TEXT="notesElevesMati&#xe8;res=pd.read_csv(&apos;C:/Users/loicm/datasets/eleves.csv&apos;,sep=&quot;|&quot;,dtype={&apos;&#xe9;l&#xe8;ve&apos;:str,&apos;moyenneMath&apos;:float,&apos;moyennePhysique&apos;:str,&apos;sexe&apos;:str,&apos;dateNaissance&apos;:str})&#xa;"/>
</node>
<node CREATED="1556959113309" FOLDED="true" ID="ID_1713504240" MODIFIED="1556993920327" TEXT="R  READR">
<node CREATED="1556961481436" ID="ID_149740616" MODIFIED="1556961616276" TEXT="notesElevesMati&#xe8;res&lt;-read_delim(&quot;C:/Users/loicm/datasets/eleves.csv&quot;,delim=&quot;|&quot;,col_types=cols(&#xe9;l&#xe8;ve = col_character(),moyenneMath=col_double(), moyennePhysique= col_character(),sexe= col_character(),dateNaissance= col_character()))&#xa;"/>
</node>
</node>
</node>
<node CREATED="1556962099160" FOLDED="true" ID="ID_1757500723" MODIFIED="1556974785581" TEXT="suppression doublons">
<node CREATED="1556962109323" FOLDED="true" ID="ID_1748075176" MODIFIED="1556974780230" TEXT="PYTHON PANDAS">
<node CREATED="1556962129444" ID="ID_1788862656" MODIFIED="1556962130872" TEXT="notesElevesMati&#xe8;res.drop_duplicates([&apos;&#xe9;l&#xe8;ve&apos;],inplace=True)"/>
</node>
<node CREATED="1556962113940" FOLDED="true" ID="ID_231190923" MODIFIED="1556974783896" TEXT="R DYPLR">
<node CREATED="1556962145148" ID="ID_1506051684" MODIFIED="1556962146868" TEXT="notesElevesMati&#xe8;res=notesElevesMati&#xe8;res %&gt;% distinct(&#xe9;l&#xe8;ve,.keep_all=TRUE)"/>
</node>
</node>
<node CREATED="1556964813506" FOLDED="true" ID="ID_351792062" MODIFIED="1556974141660" TEXT="conversion de type">
<node CREATED="1556964830058" ID="ID_1739782738" LINK="ensemble/conversions.py" MODIFIED="1556969718219" TEXT="PYTHON PANDAS"/>
<node CREATED="1556964857746" ID="ID_1136290102" LINK="ensemble/conversions.r" MODIFIED="1556972243927" TEXT="R BASE"/>
</node>
<node CREATED="1556975075792" FOLDED="true" ID="ID_870088450" MODIFIED="1556992951110" TEXT="&#xe9;crire du SQL ">
<node CREATED="1556975089282" ID="ID_1173950124" LINK="ensemble/sqlSurDataframe.R" MODIFIED="1556975414792" TEXT="R package sqldf"/>
<node CREATED="1556975709126" ID="ID_645804148" LINK="https://github.com/airtoxin/pysqldf" MODIFIED="1556975750514" TEXT="PYTHON pysqldf"/>
</node>
<node CREATED="1556992952478" FOLDED="true" ID="ID_1771686829" MODIFIED="1556993916401" TEXT="SELECT du SQL sur dataframe">
<node CREATED="1556992964932" ID="ID_873174528" MODIFIED="1556992977121" TEXT="PYTHON PANDAS =&gt; selectionColonnesDataframe=tips[[&apos;tip&apos;, &apos;sex&apos;]]"/>
<node CREATED="1556993008120" ID="ID_1761860756" MODIFIED="1556993092075" TEXT="R DPLYR =&gt; selectionColonnesDataframe=select(tips, tip, sex)"/>
</node>
<node CREATED="1556993099947" FOLDED="true" ID="ID_929006179" MODIFIED="1556993934235" TEXT="WHERE du SQL sur dataframe">
<node CREATED="1556993110276" FOLDED="true" ID="ID_1805405678" MODIFIED="1556993912844" TEXT="PYTHON PANDAS">
<node CREATED="1556993139431" ID="ID_590805802" MODIFIED="1556993145562" TEXT="ET =&gt; selectionLignesRespectantDeuxConditions=tips[(tips[&apos;total_bill&apos;]&gt;20) &amp; (tips[&apos;tip&apos;]&gt;3)]"/>
<node CREATED="1556993146176" ID="ID_96960140" MODIFIED="1556993158206" TEXT="OU =&gt; selectionLignesRespectantAuMoinsUneCondition=tips[(tips[&apos;total_bill&apos;]&gt;20) | (tips[&apos;tip&apos;]&gt;3)]"/>
<node CREATED="1556993585547" ID="ID_725151563" MODIFIED="1556993892624" TEXT="garder lignes avec NA =&gt; uneConditionEtGarderValeursManquantes=df[(df[&apos;x&apos;].isna()) | (df[&apos;x&apos;]&gt;1)]"/>
</node>
<node CREATED="1556993159549" FOLDED="true" ID="ID_204172628" MODIFIED="1556993914147" TEXT="R DPLYR">
<node CREATED="1556993240691" ID="ID_1891733237" MODIFIED="1556993311278" TEXT="ET =&gt; selectionLignesRespectantDeuxConditions= filter(tips, total_bill &gt;20 &amp;  tip&gt;3)"/>
<node CREATED="1556993312550" ID="ID_949482905" MODIFIED="1556993342720" TEXT="OU =&gt; selectionLignesRespectantAuMoinsUneCondition=filter(tips, total_bill &gt;20 |  tip&gt;3)"/>
<node CREATED="1556993556405" ID="ID_346472005" MODIFIED="1556993898833" TEXT="garder lignes avec NA =&gt; uneConditionEtGarderValeursManquantes=filter(df, is.na(x) | x &gt; 1)"/>
</node>
</node>
<node CREATED="1556974146882" FOLDED="true" ID="ID_1219498495" MODIFIED="1556993419637" TEXT="ORDER BY du SQL sur dataframe">
<node CREATED="1556974152761" FOLDED="true" ID="ID_630744418" MODIFIED="1556974778312" TEXT="PYTHON PANDAS">
<node CREATED="1556974163584" ID="ID_31437255" MODIFIED="1556974432888" TEXT="tips.sort_values([&apos;sex&apos;, &apos;total_bill&apos;],ascending=[True,False],inplace=True)"/>
</node>
<node CREATED="1556974745531" FOLDED="true" ID="ID_615921739" MODIFIED="1556993393132" TEXT="R DPLYR">
<node CREATED="1556974758640" ID="ID_1735861963" MODIFIED="1556974760307" TEXT="tips=arrange(tips,sex,desc(total_bill))"/>
</node>
</node>
<node CREATED="1556972770525" ID="ID_782104042" MODIFIED="1556994573570" TEXT="jointures du SQL sur dataframe">
<node CREATED="1556972776808" ID="ID_1303215842" LINK="ensemble/jointures.py" MODIFIED="1556972788978" TEXT="PYTHON PANDAS"/>
<node CREATED="1556972790648" ID="ID_1060518155" LINK="ensemble/jointures.R" MODIFIED="1556974018350" TEXT="R"/>
</node>
</node>
</node>
</map>
