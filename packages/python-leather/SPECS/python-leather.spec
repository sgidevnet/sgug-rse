%{?python_enable_dependency_generator}
%global pypi_name leather
%global dir_name leather
%global project_owner wireservice
%global github_name leather
%global commit e85dd30cc20270180c26c56fd895aff61e84f741
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global desc Leather is the Python charting library for those who need charts now and don’t\
care if they’re perfect.\
\
- A readable and user-friendly API.\
- Optimized for exploratory charting.\
- Produces scale-independent SVG charts.\
- Completely type-agnostic. Chart your data, whatever it is.\
- Designed with iPython, Jupyter and atom/hydrogen in mind.\
- Pure Python. No C dependencies to compile.


Name:           python-%{pypi_name}
Version:        0.3.3
Release:        16.git%{shortcommit}%{?dist}
Summary:        Python charting for 80% of humans

License:        MIT
URL:            https://pypi.python.org/pypi/leather
Source0:        https://github.com/%{project_owner}/%{github_name}/archive/%{commit}/%{github_name}-%{commit}.tar.gz
BuildArch:      noarch

%description
%{desc}


%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-nose >= 1.1.2
BuildRequires:  python3-sphinx >= 1.2.2
BuildRequires:  python3-coverage >= 3.7.1
BuildRequires:  python3-sphinx_rtd_theme >= 0.1.6
BuildRequires:  python3-lxml >= 3.6.0
BuildRequires:  python3-six >= 1.6.1
BuildRequires:  python3-cssselect
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{desc}


%package -n    python-%{pypi_name}-doc
Summary:       %{summary}

%description -n python-%{pypi_name}-doc
%{desc}

Documentation package.


%prep
%setup -qn %{github_name}-%{commit}
# Remove shebang on non executable scripts
sed -i '1{\@^#!/usr/bin/env python@d}' leather/*.py leather/**/*.py

# Remove hidden files in examples
rm examples/charts/.placeholder

%build
%py3_build
pushd docs
    make html
    # Remove hidden file
    rm _build/html/.buildinfo
popd


%install
%py3_install


%check
nosetests-%{python3_version} tests -v


%files -n python3-%{pypi_name}
%doc README.rst
%license COPYING
%{python3_sitelib}/%{dir_name}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/%{dir_name}/


%files -n python-%{pypi_name}-doc
%doc examples docs/_build/html
%license COPYING


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-16.gite85dd30
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-15.gite85dd30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan  9 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.3.3-14.gite85dd30
- Remove dependency on unittest2 (#1789200)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-13.gite85dd30
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-12.gite85dd30
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-11.gite85dd30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-10.gite85dd30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.3-9.gite85dd30
- Enable python dependency generator

* Mon Jan 14 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-8.gite85dd30
- Subpackage python2-leather has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-7.gite85dd30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-6.gite85dd30
- Rebuilt for Python 3.7

* Thu Mar 15 2018 Julien Enselme <jujens@jujens.eu> - 0.3.3-5.gite85dd30
- Correct build dependencies

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-4.gite85dd30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-3.gite85dd30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 14 2017 Julien Enselme <jujens@jujens.eu> - 0.3.3-2.gite85dd30
- Remove uneeded BuildArch
- Don't use sed inside a loop, pass the expression with globs directly to sed.
- Improve description

* Tue Jan 03 2017 Julien Enselme <jujens@jujens.eu> - 0.3.3-1.gite85dd30
- Inital package
