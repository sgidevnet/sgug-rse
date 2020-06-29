%global pypi_name speedtest-cli

Name:		python-%{pypi_name}
Version:	2.1.2
Release:	3%{?dist}
Summary:	Command-line interface for testing internet bandwidth using speedtest.net

License:	ASL 2.0
URL:		https://github.com/sivel/speedtest-cli
Source0:	https://github.com/sivel/speedtest-cli/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	help2man

%description
%{summary}.

%package -n python3-%{pypi_name}
Summary:	%{summary}

BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{summary}.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%{__mkdir} -p %{buildroot}%{_mandir}/man1
%py3_install
export PYTHONPATH="%{buildroot}%{python3_sitelib}"
for f in $(%{_bindir}/find %{buildroot}%{_bindir} -type f -name '*' | /bin/sort )
do
	of="$(/bin/basename ${f}).1"
	%{_bindir}/help2man -s 1 -N -o %{buildroot}%{_mandir}/man1/${of} ${f}
done
unset PYTHONPATH

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{_bindir}/speedtest*
%{_mandir}/man1/speedtest*.1*
%{python3_sitelib}/speedtest*.py
%{python3_sitelib}/speedtest_cli-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/__pycache__/speedtest*.cpython-%{python3_version_nodots}*.pyc

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.2-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 16 2019 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.2-1
- Update to latest upstream release 2.1.2
- Remove support for Python 2 (rhbz#1740994)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-5
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.2-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 20 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.2-1
- Initial import (rhbz#1425203)

* Mon Feb 20 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.2-0.1
- Initial rpm-release (rhbz#1425203)
