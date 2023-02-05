%global pypi_name sipvicious

Name:           %{pypi_name}
Version:        0.3.0
Release:        1%{?dist}
Summary:        Set of tools to audit SIP based VoIP systems

License:        GPLv3+
URL:            https://github.com/EnableSecurity/sipvicious
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
The SIPVicious OSS toolset consists of the following tools:

- svmap
- svwar
- svcrack
- svreport
- svcrash

%package -n     python3-%{pypi_name}
Summary:        Python module of %{pypi_name}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python module of %{pypi_name}.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
# Remove shebang: https://github.com/EnableSecurity/sipvicious/pull/57
sed -i -e '/^#!\//, 1d' sipvicious/{svcrack,svcrash,svmap,svreport,svwar}.py
sed -i -e '/^#!\//, 1d' sipvicious/{libs/pptable,libs/svhelper}.py

%build
%py3_build

%install
%py3_install
# https://github.com/EnableSecurity/sipvicious/pull/58
for PAGE in man1/svcrack.1 man1/svcrash.1 man1/svmap.1 man1/svreport.1 man1/svwar.1; do
  install -Dp -m 0644 $PAGE %{buildroot}%{_mandir}/$PAGE
done

%files
%doc README.md
%{_mandir}/man1/sv*.*
%{_bindir}/sipvicious_svcrack
%{_bindir}/sipvicious_svcrash
%{_bindir}/sipvicious_svmap
%{_bindir}/sipvicious_svreport
%{_bindir}/sipvicious_svwar

%files -n python3-%{pypi_name}
%doc Changelog README.md THANKS TODO
# https://github.com/EnableSecurity/sipvicious/pull/55
#%%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon May 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.0-1
- Initial package for Fedora
