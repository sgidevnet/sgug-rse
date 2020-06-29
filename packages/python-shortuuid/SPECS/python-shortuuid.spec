Name:           python-shortuuid
Version:        1.0.1
Release:        2%{?dist}
Summary:        A generator library for concise, unambiguous and URL-safe UUIDs
License:        BSD
URL:            https://github.com/stochastic-technologies/shortuuid/
Source0:        https://pypi.python.org/packages/80/d7/2bfc9332e68d3e15ea97b9b1588b3899ad565120253d3fd71c8f7f13b4fe/shortuuid-%{version}.tar.gz

BuildArch: noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
A library that generates short, pretty, unambiguous unique IDs by using an 
extensive, case-sensitive alphabet and omitting similar-looking letters and 
numbers.

%package -n python3-shortuuid
Summary:        A generator library for concise, unambiguous and URL-safe UUIDs
%{?python_provide:%python_provide python3-shortuuid}

%description -n python3-shortuuid
A library that generates short, pretty, unambiguous unique IDs by using an 
extensive, case-sensitive alphabet and omitting similar-looking letters and 
numbers.

%prep
%autosetup -p1 -n shortuuid-%{version}

%build
rm -rf shortuuid.egg-info
%py3_build

%install
%py3_install

%files -n python3-shortuuid
%license COPYING
%{python3_sitelib}/shortuuid-%{version}*
%{python3_sitelib}/shortuuid/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-2
- Rebuilt for Python 3.9

* Sat Mar 07 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1

* Fri Mar 06 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.5.0-7
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.5.0-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar  1 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.5.0-1
- Update to 0.5.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan  7 2017 Peter Robinson <pbrobinson@fedoraproject.org> 3.0.1-1
- initial packaging
