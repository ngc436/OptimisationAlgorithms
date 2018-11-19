from data_utils import create_matrix, read_tsp_file
from GA_tsp_optimisation import ga_pipeline
from hyperopt import fmin, tpe, hp, STATUS_OK, Trials

fname = 'xqf131.tsp'

matrix = create_matrix(fname)
coord = read_tsp_file(fname)


def ga_wrapper(params):
    population_size = int(params['population_size'])
    best_perc = params['best_perc']
    mutation_rate = params['mutation_rate']
    mutation_intensity = params['mutation_intensity']
    val = ga_pipeline(mat=matrix, population_size=population_size,
                      best_perc=best_perc, mutation_rate=mutation_rate,
                      mutation_intensity=mutation_intensity, generations=4000,
                      verbose=0, plot=0)
    print(params, val)
    return {'loss': val, 'status': STATUS_OK}


def hyperopt_optimization():
    trials = Trials()

    space = {
        'best_perc': hp.uniform('best_perc', 0.3, 0.9),
        'population_size': hp.quniform('population_size', 100, 100, 1),
        'mutation_rate': hp.uniform('mutation_rate', 0.1, 0.8),
        'mutation_intensity': hp.uniform('mutation_intensity', 0.1, 0.7)
    }

    best = fmin(
        ga_wrapper,
        space=space,
        algo=tpe.suggest,
        max_evals=100,
        trials=trials
    )

    return best


def run_tsp(population_size, best_perc, mutation_rate, mutation_intensity, genetations, coord):
    val = ga_pipeline(mat=matrix, population_size=population_size,
                      best_perc=best_perc, mutation_rate=mutation_rate,
                      generations=genetations, verbose=1, coord=coord,
                      mutation_intensity=mutation_intensity, plot=1)
    return val


def main():
    print(hyperopt_optimization())
    # print(
    #     run_tsp(mutation_rate=0.4, best_perc=0.4,
    #             population_size=100, genetations=100000, coord=coord,
    #             mutation_intensity=0.3))


if __name__ == '__main__':
    main()
#
# {'best_perc': 0.3353487325730243, 'population_size': 100.0, 'mutation_intensity': 0.1637290967546366, 'mutation_rate': 0.7699072655870585} 2034.240893719069
# {'best_perc': 0.5070068560653156, 'population_size': 100.0, 'mutation_intensity': 0.6686125822263597, 'mutation_rate': 0.6745882299583341} 2390.71266649068
# {'best_perc': 0.3121718601287198, 'population_size': 100.0, 'mutation_intensity': 0.3738266360515896, 'mutation_rate': 0.7858731033423696} 2101.001664704916
# {'best_perc': 0.6159947499030161, 'population_size': 100.0, 'mutation_intensity': 0.14302302350662952, 'mutation_rate': 0.7730383199939405} 1962.8546950190264
# {'best_perc': 0.6732336453130217, 'population_size': 100.0, 'mutation_intensity': 0.5197999898452123, 'mutation_rate': 0.3665923821696868} 2968.9345789084223
# {'best_perc': 0.5708442339611306, 'population_size': 100.0, 'mutation_intensity': 0.12314528850241085, 'mutation_rate': 0.41467091413618196} 2035.2721326878834
# {'best_perc': 0.6074272077955342, 'population_size': 100.0, 'mutation_intensity': 0.4053327350727963, 'mutation_rate': 0.23241440447500963} 2520.8328354845294
# {'best_perc': 0.7184715766402554, 'population_size': 100.0, 'mutation_intensity': 0.1969872762514762, 'mutation_rate': 0.6531975548490033} 2174.9712262902913
# {'best_perc': 0.4550353764169712, 'population_size': 100.0, 'mutation_intensity': 0.5143244608504861, 'mutation_rate': 0.6145132622309759} 2504.237439651352
# {'best_perc': 0.8704425070459987, 'population_size': 100.0, 'mutation_intensity': 0.4511064400977748, 'mutation_rate': 0.22826987764204074} 3000.0214049221645
# {'best_perc': 0.6024751492005977, 'population_size': 100.0, 'mutation_intensity': 0.4064511678297936, 'mutation_rate': 0.4858052700560761} 2371.4211966551097
# {'best_perc': 0.7457165203773737, 'population_size': 100.0, 'mutation_intensity': 0.30742411278518916, 'mutation_rate': 0.1699764474585712} 2874.738661471816
# {'best_perc': 0.42829243452821353, 'population_size': 100.0, 'mutation_intensity': 0.3838454556833788, 'mutation_rate': 0.30359611111365953} 2632.248776478962
# {'best_perc': 0.7469335793029386, 'population_size': 100.0, 'mutation_intensity': 0.5673778054212364, 'mutation_rate': 0.5799971143222805} 2503.192952175029
# {'best_perc': 0.7822598489199468, 'population_size': 100.0, 'mutation_intensity': 0.6364797256727458, 'mutation_rate': 0.6910026850354992} 2879.798678795492
# {'best_perc': 0.6906988604709555, 'population_size': 100.0, 'mutation_intensity': 0.35263022530491284, 'mutation_rate': 0.7407448888770896} 2309.5169341121664
# {'best_perc': 0.5445467852667065, 'population_size': 100.0, 'mutation_intensity': 0.2794765122083883, 'mutation_rate': 0.337837195275992} 2505.859896978876
# {'best_perc': 0.7527780266157553, 'population_size': 100.0, 'mutation_intensity': 0.17930434348525873, 'mutation_rate': 0.285361215025237} 2262.7747486350245
# {'best_perc': 0.36430248348738625, 'population_size': 100.0, 'mutation_intensity': 0.581852405479275, 'mutation_rate': 0.4962688641019595} 2632.50380845073
# {'best_perc': 0.5772345966408154, 'population_size': 100.0, 'mutation_intensity': 0.3766042603046722, 'mutation_rate': 0.5979740359481615} 2463.6240293341234