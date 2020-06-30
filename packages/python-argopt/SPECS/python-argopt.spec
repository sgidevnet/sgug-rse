%{?python_enable_dependency_generator}
%global srcname argopt
%global _description \
Define your command line interface (CLI) from a docstring\
(rather than the other way around). Because it’s easy. It’s quick.\
Painless. Then focus on what’s actually important - using the arguments\
in the rest of your program.

Name:           python-%{srcname}
Version:        0.4.0
Release:        8%{?dist}
Summary:        Doc to argparse driven by docopt

License:        MPLv2.0
URL:            https://github.com/casperdcl/argopt
Source0:        %{pypi_source}

BuildArch:      noarch

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version}
rm -vrf *.egg-info
# https://github.com/casperdcl/argopt/issues/6
sed -i -e "/install_requires/d" setup.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENCE
%doc README.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 24 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.0-2
- Enable python dependency generator

* Mon Sep 24 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.0-1
- Initial package
