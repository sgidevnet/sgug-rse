%{?python_enable_dependency_generator}

%global pypi_name agate
%global project_owner wireservice
%global github_name agate
%global desc agate is a Python data analysis library that is optimized for humans instead \
of machines. It is an alternative to numpy and pandas that solves real-world \
problems with readable code.\
\
agate was previously known as journalism.


Name:           python-%{pypi_name}
Version:        1.6.1
Release:        10%{?dist}
Summary:        Data analysis library that is optimized for humans instead of machines

License:        MIT
URL:            https://pypi.python.org/pypi/agate
Source0:        https://github.com/%{project_owner}/%{github_name}/archive/%{version}/%{github_name}-%{version}.tar.gz
BuildArch:      noarch

%description
%{desc}


%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-nose
BuildRequires:  python3-coverage >= 3.7.1
BuildRequires:  python3-mock >= 1.3.0
BuildRequires:  python3-lxml >= 3.6.0
BuildRequires:  python3-cssselect
BuildRequires:  python3dist(six) >= 1.9
BuildRequires:  python3dist(pytimeparse) >= 1.1.5
BuildRequires:  python3dist(parsedatetime) >= 2.1
BuildRequires:  python3dist(babel) >= 2
BuildRequires:  python3dist(isodate) >= 0.5.4
BuildRequires:  python3dist(python-slugify) >= 1.2.1
BuildRequires:  python3dist(leather) >= 0.3.
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{desc}


%package -n    python-%{pypi_name}-doc
Summary:       %{summary}
BuildRequires:  python3dist(sphinx) >= 1.2.2
BuildRequires:  python3dist(sphinx-rtd-theme) >= 0.1.6
BuildArch:     noarch

%description -n python-%{pypi_name}-doc
%{desc}

Documentation package.


%prep
%setup -qn %{github_name}-%{version}
# Remove shebang on non executable scripts
sed -i '1{\@^#!/usr/bin/env python@d}' agate/*.py agate/**/*.py
# In agate/testcase.py the interpretor name starts with a capital letter.
sed -i '1{\@^#!/usr/bin/env Python@d}' agate/testcase.py


%build
%py3_build

# Build documentation
pushd docs
    make html SPHINXBUILD=sphinx-build-%{python3_version}
    rm -f _build/html/.buildinfo
popd


%install
%py3_install


%check
nosetests-%{python3_version} tests -v


%files -n python3-%{pypi_name}
%doc README.rst AUTHORS.rst CHANGELOG.rst
%license COPYING
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/%{pypi_name}/


%files -n python-%{pypi_name}-doc
%license COPYING
%doc README.rst AUTHORS.rst CHANGELOG.rst docs/_build/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.6.1-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.6.1-8
- Remove dependency on unittest2 (#1789200)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.1-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 02 2019 Julien Enselme <jujens@jujens.eu> - 1.6.1-4
- Remove Python 2 subpackage
- Enable python dependency generator

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.6.1-2
- Rebuilt for Python 3.7

* Mon Mar 12 2018 Julien Enselme <jujens@jujens.eu> - 1.6.1-1
- Update to 1.6.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4.gited9e179
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.6.0-3.gited9e179
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)
- BR python{2,3}-cssselect for tests

* Mon Aug 21 2017 Julien Enselme <jujens@jujens.eu> - 1.6.0-2.gited9e179
- Add python-unittest2 to BR for tests to pass on koji

* Sun Mar 12 2017 Julien Enselme <jujens@jujens.eu> - 1.6.0-1.gited9e179
- Inital package
