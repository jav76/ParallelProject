import math
from mpmath import *

mp.dps = 100000

E_CONST_STR = """2.718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427427466391932003059921817413596629043572900334295260595630738132328627943490763233829880753195251019011573834187930702154089149934884167509244761460668082264800168477411853742345442437107539077744992069551702761838606261331384583000752044933826560297606737113200709328709127443747047230696977209310141692836819025515108657463772111252389784425056953696770785449969967946864454905987931636889230098793127736178215424999229576351482208269895193668033182528869398496465105820939239829488793320362509443117301238197068416140397019837679320683282376464804295311802328782509819455815301756717361332069811250996181881593041690351598888519345807273866738589422879228499892086805825749279610484198444363463244968487560233624827041978623209002160990235304369941849146314093431738143640546253152096183690888707016768396424378140592714563549061303107208510383750510115747704171898610687396965521267154688957035035402123407849819334321068170121005627880235193033224745015853904730419957777093503660416997329725088687696640355570716226844716256079882651787134195124665201030592123667719432527867539855894489697096409754591856956380236370162112047742722836489613422516445078182442352948636372141740238893441247963574370263755294448337998016125492278509257782562092622648326277933386566481627725164019105900491644998289315056604725802778631864155195653244258698294695930801915298721172556347546396447910145904090586298496791287406870504895858671747985466775757320568128845920541334053922000113786300945560688166740016984205580403363795376452030402432256613527836951177883863874439662532249850654995886234281899707733276171783928034946501434558897071942586398772754710962953741521115136835062752602326484728703920764310059584116612054529703023647254929666938115137322753645098889031360205724817658511806303644281231496550704751025446501172721155519486685080036853228183152196003735625279449515828418829478761085263981395599006737648292244375287184624578036192981971399147564488262603903381441823262515097482798777996437308997038886778227138360577297882412561190717663946507063304527954661855096666185664709711344474016070462621568071748187784437143698821855967095910259686200235371858874856965220005031173439207321139080329363447972735595527734907178379342163701205005451326383544000186323991490705479778056697853358048966906295119432473099587655236812859041383241160722602998330535370876138939639177957454016137223618789365260538155841587186925538606164779834025435128439612946035291332594279490433729908573158029095863138268329147711639633709240031689458636060645845925126994655724839186564209752685082307544254599376917041977780085362730941710163434907696423722294352366125572508814779223151974778060569672538017180776360346245927877846585065605078084421152969752189087401966090665180351650179250461950136658543663271254963990854914420001457476081930221206602433009641270489439039717719518069908699860663658323227870937650226014929101151717763594460202324930028040186772391028809786660565118326004368850881715723866984224220102495055188169480322100251542649463981287367765892768816359831247788652014117411091360116499507662907794364600585194199856016264790761532103872755712699251827568798930276176114616254935649590379804583818232336861201624373656984670378585330527583333793990752166069238053369887956513728559388349989470741618155012539706464817194670834819721448889879067650379590366967249499254527903372963616265897603949857674139735944102374432970935547798262961459144293645142861715858733974679189757121195618738578364475844842355558105002561149239151889309946342841393608038309166281881150371528496705974162562823609216807515017772538740256425347087908913729172282861151591568372524163077225440633787593105982676094420326192428531701878177296023541306067213604600038966109364709514141718577701418060644363681546444005331608778314317444081194942297559931401188868331483280270655383300469329011574414756313999722170380461709289457909627166226074071874997535921275608441473782330327033016823719364800217328573493594756433412994302485023573221459784328264142168487872167336701061509424345698440187331281010794512722373788612605816566805371439612788873252737389039289050686532413806279602593038772769778379286840932536588073398845721874602100531148335132385004782716937621800490479559795929059165547050577751430817511269898518840871856402603530558373783242292418562564425502267215598027401261797192804713960068916382866527700975276706977703643926022437284184088325184877047263844037953016690546593746161932384036389313136432713768884102681121989127522305625675625470172508634976536728860596675274086862740791285657699631378975303466061666980421826772456053066077389962421834085988207186468262321508028828635974683965435885668550377313129658797581050121491620765676995065971534476347032085321560367482860837865680307306265763346977429563464371670939719306087696349532884683361303882943104080029687386911706666614680001512114344225602387447432525076938707777519329994213727721125884360871583483562696166198057252661220679754062106208064988291845439530152998209250300549825704339055357016865312052649561485724925738620691740369521353373253166634546658859728665945113644137033139367211856955395210845840724432383558606310680696492485123263269951460359603729725319836842336390463213671011619282171115028280160448805880238203198149309636959673583274202498824568494127386056649135252670604623445054922758115170931492187959271800194096886698683703730220047531433818109270803001720593553052070070607223399946399057131158709963577735902719628506114651483752620956534671329002599439766311454590268589897911583709341937044115512192011716488056694593813118384376562062784631049034629395002945834116482411496975832601180073169943739350696629571241027323913874175492307186245454322203955273529524024590380574450289224688628533654221381572213116328811205214648980518009202471939171055539011394331668151582884368760696110250517100739276238555338627255353883096067164466237092264680967125406186950214317621166814009759528149390722260111268115310838731761732323526360583817315103459573653822353499293582283685100781088463434998351840445170427018938199424341009057537625776757111809008816418331920196262341628816652137471732547772778348877436651882875215668571950637193656539038944936642176400312152787022236646363575550356557694888654950027085392361710550213114741374410613444554419210133617299628569489919336918472947858072915608851039678195942983318648075608367955149663644896559294818785178403877332624705194505041984774201418394773120281588684570729054405751060128525805659470304683634459265255213700806875200959345360731622611872817392807462309468536782310609792159936001994623799343421068781349734695924646975250624695861690917857397659519939299399556754271465491045686070209901260681870498417807917392407194599632306025470790177452751318680998228473086076653686685551646770291133682756310722334672611370549079536583453863719623585631261838715677411873852772292259474337378569553845624680101390572787101651296663676445187246565373040244368414081448873295784734849000301947788802046032466084287535184836495919508288832320652212810419044804724794929134228495197002260131043006241071797150279343326340799596053144605323048852897291765987601666781193793237245385720960758227717848336161358261289622611812945592746276713779448758675365754486140761193112595851265575973457301533364263076798544338576171533346232527057200530398828949903425956623297578248873502925916682589445689465599265845476269452878051650172067478541788798227680653665064191097343452887833862172615626958265447820567298775642632532159429441803994321700009054265076309558846589517170914760743713689331946909098190450129030709956622662030318264936573369841955577696378762491885286568660760056602560544571133728684020557441603083705231224258722343885412317948138855007568938112493538631863528708379984569261998179452336408742959118074745341955142035172618420084550917084568236820089773945584267921427347756087964427920270831215015640634134161716644806981548376449157390012121704154787259199894382536495051477137939914720521952907939613762110723849429061635760459623125350606853765142311534966568371511660422079639446662116325515772907097847315627827759878813649195125748332879377157145909106484164267830994972367442017586226940215940792448054125536043131799269673915754241929660731239376354213923061787675395871143610408940996608947141834069836299367536262154524729846421375289107988438130609555262272083751862983706678722443019579379378607210725427728907173285487437435578196651171661833088112912024520404868220007234403502544820283425418788465360259150644527165770004452109773558589762265548494162171498953238342160011406295071849042778925855274303522139683567901807640604213830730877446017084268827226117718084266433365178000217190344923426426629226145600433738386833555534345300426481847398921562708609565062934040526494324426144566592129122564889356965500915430642613425266847259491431423939884543248632746184284665598533231221046625989014171210344608427161661900125719587079321756969854401339762209674945418540711844643394699016269835160784892451405894094639526780735457970030705116368251948770118976400282764841416058720618418529718915401968825328930914966534575357142731848201638464483249903788606900807270932767312758196656394114896171683298045513972950668760474091542042842999354102582911350224169076943166857424252250902693903481485645130306992519959043638402842926741257342244776558417788617173726546208549829449894678735092958165263207225899236876845701782303809656788311228930580914057261086588484587310165815116753332767488701482916741970151255978257270740643180860142814902414678047232759768426963393577354293018673943971638861176420900406866339885684168100387238921448317607011668450388721236436704331409115573328018297798873659091665961240202177855885487617616198937079438005666336488436508914480557103976521469602766258359905198704230017946553679"""
E_CONST = mpf(E_CONST_STR)

def check_error(approx):
    approx = mpf(approx)
    error = E_CONST - approx
    return error

def check_precision(error):
    error_str = str(error)
    error_str = error_str[2:]
    decimals = 0
    for i in error_str:
        if i == '0':
            decimals = decimals + 1
        else:
            break
    return decimals

def euler_approximation(n):
    sum = mpf(1)
    for i in range(1, n):
        sum = sum + mpf(1) / mpf(math.factorial(i))
    return sum

if __name__ == '__main__':

    #nprint(mpf(E_CONST), 10000)
    a = euler_approximation(4000)
    print(check_precision((check_error(a))))


