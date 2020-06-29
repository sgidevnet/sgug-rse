%bcond_without tests
%bcond_with docs

%global srcname pingouin

%global _description %{expand:
Pingouin is an open-source statistical package written in Python 3 and based on
Pandas and NumPy.

It provides easy-to-grasp functions for computing several statistical
functions:

- ANOVAs: one- and two-ways, repeated measures, mixed, ancova
- Post-hocs tests and pairwise comparisons
- Robust correlations
- Partial correlation, repeated measures correlation and intraclass correlation
- Bayes Factor
- Tests for sphericity, normality and homoscedasticity
- Effect sizes (Cohen's d, Hedges'g, AUC, Glass delta, eta-square...)
- Parametric/bootstrapped confidence intervals around an effect size or a
  correlation coefficient
- Circular statistics
- Linear/logistic regression and mediation analysis

Pingouin is designed for users who want simple yet exhaustive statistical
functions.}

Name:           python-%{srcname}
Version:        0.3.5
Release:        2%{?dist}
Summary:        Statistical package for Python

# Documentation pulls in bootstrap, bootswatch, jquery which are MIT
License:        GPLv3 and MIT
URL:            https://pypi.python.org/pypi/%{srcname}
# Pypi tar does not contain docs and tests
Source0:        https://github.com/raphaelvallat/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel

BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist pandas}
BuildRequires:  %{py3_dist seaborn}
BuildRequires:  %{py3_dist setuptools}

%if %{with tests}
BuildRequires:  %{py3_dist pandas-flavor}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-cov}
BuildRequires:  %{py3_dist pytest-remotedata}
BuildRequires:  %{py3_dist statsmodels}
BuildRequires:  %{py3_dist pytest-sugar}
BuildRequires:  %{py3_dist outdated}
BuildRequires:  %{py3_dist openpyxl}
BuildRequires:  %{py3_dist mpmath}
BuildRequires:  %{py3_dist scikit-learn}
BuildRequires:  %{py3_dist tabulate}
# Only required and works in TRAVIS, so not needed here
# BuildRequires:  python3-pytest-travis-fold
%endif

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%package doc
Summary:        %{summary}
BuildRequires:  %{py3_dist numpydoc}
BuildRequires:  %{py3_dist pandas-flavor}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-bootstrap-theme}

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info

%build
%py3_build

%if %{with docs}
PYTHONPATH=. sphinx-build-%{python3_version} -b html docs html
rm -rf html/.doctrees
rm -rf html/.buildinfo
rm -rf html/.nojekyll
%endif

%install
%py3_install

%check
%if %{with tests}
export PYTHONPATH=%{buildroot}%{python3_sitelib}
pytest-%{python3_version}
%endif

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{srcname}

%files doc
%license LICENSE
%doc notebooks
%if %{with docs}
%doc html
%endif

%changelog
* Thu Jun 25 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.3.5-2
- Explicitly BR setuptools

* Sun Jun 21 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.3.5-1
- Update to 0.3.5

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-2
- Rebuilt for Python 3.9

* Sat May 02 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.3.3-1
- Update to latest release

* Fri Dec 06 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.3.1-1
- Update to 0.3.1

* Sat Nov 09 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.9-1
- Update to 0.2.9
- rebuild since scipy 1.3.0 is now available in rawhide
- Requires pandas-flavor, needs packaging

* Sat Jul 20 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.7-1
- Correct license
- Add missing BR
- Add notebooks to documentation

* Fri Jul 19 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.7-1
- Initial build
