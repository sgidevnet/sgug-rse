# Docs fail to build
# Reported: https://github.com/NeuralEnsemble/elephant/issues/228
%bcond_with docs

%global pypi_name elephant

%define _binaries_in_noarch_packages_terminate_build   0

Name:       python-%{pypi_name}
Version:    0.6.4
Release:    3%{?dist}
Summary:    Elephant is a package for analysis of electrophysiology data in Python
License:    BSD
URL:        http://neuralensemble.org/elephant
# Must use github tarball. Test data not included in pypi tar
# https://github.com/NeuralEnsemble/elephant/issues/225
Source0:    https://github.com/neuralensemble/%{pypi_name}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:  noarch

# Remove bits from setup.py that try to download fim.
# we use the packaged version
# Patch0:     0001-Do-not-download-fim-so.patch

BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3dist(neo)
BuildRequires:  python3dist(nose)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pandas)
BuildRequires:  python3dist(quantities)
BuildRequires:  python3dist(scikit-learn)
BuildRequires:  python3dist(scipy)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(fim)

%if %{with docs}
BuildRequires:  python3dist(nbsphinx)
BuildRequires:  python3dist(numpydoc)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3dist(sphinx-gallery)
BuildRequires:  python3dist(sphinxcontrib-bibtex)
%endif

%description
Elephant - Electrophysiology Analysis Toolkit Elephant is a package for the
analysis of neurophysiology data, based on Neo.

%{?python_enable_dependency_generator}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Elephant - Electrophysiology Analysis Toolkit Elephant is a package for the
analysis of neurophysiology data, based on Neo.

%if %{with docs}
%package -n python-%{pypi_name}-doc
Summary:        elephant documentation

%description -n python-%{pypi_name}-doc
Documentation for elephant

%endif

%prep
%autosetup -n %{pypi_name}-%{version} -S git
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

rm -frv doc/_build

for lib in $(find . -type f -name "*.py"); do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

# remove neo version constraints
sed -i 's/neo.*/neo>=0.7.1/' requirements.txt

# Use fim from python-pyfim which is faster
sed -i 's|from elephant.spade_src import fim|import fim|' elephant/spade.py elephant/test/test_spade.py

%build
%py3_build

%if %{with docs}
pushd doc
    make SPHINXBUILD=sphinx-build-3 html
    rm -rf build/.doctrees
    rm -rf build/.buildinfo
popd
%endif

%install
%py3_install

# %check
# Ignore tests:
# test_unitary_event_analysis: tries to download data
# test_cubic: seems to fail on 32 bit machines.
# Reported upstream: https://github.com/NeuralEnsemble/elephant/issues/227
# nosetests-3 -I test_unitary_event_analysis.py -I test_cubic.py

%files -n python3-%{pypi_name}
%license LICENSE.txt elephant/spade_src/LICENSE
%doc README.md elephant/current_source_density_src/README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%if %{with docs}
%files -n python-%{pypi_name}-doc
%doc doc/_build/html
%license LICENSE.txt elephant/spade_src/LICENSE
%endif

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.4-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 23 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.6.4-1
- New upstream version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.2-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 14 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.6.2-3
- Use pyfim which is 10 times faster than the python fast_fca according to docs
- Patch out bits that try to download fim
- Version neo requirements

* Fri Jun 14 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.6.2-2
- Report issues upstream and add links to spec file

* Tue Jun 11 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.6.2-2
- Fix comment #11 BZ#1651824

* Fri Jun 07 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.6.2-1
- Initial package.
