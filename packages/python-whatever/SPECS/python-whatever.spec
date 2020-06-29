%global srcname whatever

Name:           python-%{srcname}
Version:        0.6
Release:        2%{?dist}
Summary:        Easy way to make anonymous functions by partial application of operators

License:        BSD
URL:            https://github.com/Suor/whatever
Source0:        %{pypi_source}
Source1:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
An easy way to make lambdas by partial application of python operators.

Inspired by Perl 6 one, see http://perlcabal.org/syn/S02.html#The_Whatever_Object}

%description %{_description}

%package     -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version}
rm -vr *.egg-info
tar -xvf %{S:1} --strip-components=1 --wildcards '%{srcname}-%{version}/test*' '%{srcname}-%{version}/CHANGELOG'

%build
%py3_build

%install
%py3_install

%check
%python3 -m pytest -v

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst CHANGELOG
%{python3_sitelib}/%{srcname}.py
%{python3_sitelib}/__pycache__/%{srcname}.*
%{python3_sitelib}/%{srcname}-*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6-2
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.14-1
- Initial package
