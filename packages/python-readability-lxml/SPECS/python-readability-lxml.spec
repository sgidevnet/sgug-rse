%global _python_bytecompile_errors_terminate_build 0

%global commit      ede4d015abd1829cc723ad59bf2db3c487fda66f
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date        20200326

%global pypi_name readability-lxml

Name:           python-%{pypi_name}
Version:        0.7.1
Release:        3.%{date}git%{shortcommit}%{?dist}
Summary:        Fast html to text parser (article readability tool)

License:        ASL 2.0
URL:            https://github.com/buriy/python-readability
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(chardet)
BuildRequires:  python3dist(cssselect)
BuildRequires:  python3dist(lxml)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(timeout-decorator)

%description
Given a html document, it pulls out the main body text and cleans it up.

This is a python port of a ruby port of arc90's readability project.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%?python_enable_dependency_generator

%description -n python3-%{pypi_name}
Given a html document, it pulls out the main body text and cleans it up.

This is a python port of a ruby port of arc90's readability project.


%prep
%autosetup -n python-readability-%{commit}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Remove shebang from Python libraries
for lib in readability/*.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done


%build
%py3_build


%install
%py3_install


%check
%{python3} -m pytest -v


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/readability_lxml-*-py%{python3_version}.egg-info
%{python3_sitelib}/readability/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-3.20200326gitede4d01
- Rebuilt for Python 3.9

* Thu Mar 26 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.1-2.20200326gitede4d01
- Bump to latest snapshot with LICENSE file
- Remove shebang from Python libraries

* Fri Mar 20 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.1-1.20200320git5800210
- Update to latest git snapshot (0.8beta)

* Fri Mar 20 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.1-1
- Initial package
