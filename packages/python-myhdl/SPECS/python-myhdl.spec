%global srcname myhdl
%global sum A python hardware description and verification language

Name:           python-%{srcname}
Version:        0.11
Release:        2%{?dist}
Summary:        %{sum}
License:        LGPLv2+
URL:            http://myhdl.org
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel

%description
%{name} is a Python hardware description and verification language that 
helps you go from Python to silicon. MyHDL code can be converted to Verilog 
and VHDL. It can also be used to convert signals, do co-simulation 
with Verilog, generating test benches with test vectors for VHDL, Verilog and 
supports viewing waveform by tracing signal changes in a VCD file.


%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{name} is a Python3 hardware description and verification language that 
helps you go from Python to silicon. MyHDL code can be converted to Verilog 
and VHDL. It can also be used to convert signals, do co-simulation 
with Verilog, generating test benches with test vectors for VHDL, Verilog and 
supports viewing waveform by tracing signal changes in a VCD file.


%prep
%setup -q -n myhdl-%{version}
find -name '*.txt' | xargs chmod -x

%build
%py3_build

%install
%py3_install


%files -n python3-%{srcname}
%doc /usr/share/myhdl/cosimulation/
%license LICENSE.txt
%{python3_sitelib}/*


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.11-2
- Rebuilt for Python 3.9

* Sun Apr 19 2020 Filipe Rosset <rosset.filipe@gmail.com> - 0.11-1
- Update to 0.11

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.10-2
- Subpackage python2-myhdl has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Sep 08 2018 Filipe Rosset <rosset.filipe@gmail.com> - 0.10-1
- Update to 0.10 fixes rhbz #1605788

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-2
- Rebuild for Python 3.6

* Wed Jul 27 2016 Dominika Krejci <dkrejci@redhat.com> - 0.9.0-1
- Update to 0.9.0
- Add Python3

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Aug 27 2014 Filipe Rosset <rosset.filipe@gmail.com> - 0.8.1-1
- Rebuilt for new upstream release 0.8.1, fixes rhbz #1134008

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 21 2013 Shakthi Kannan <shakthimaan [AT] fedoraproject DOT org> - 0.8-1
- Updated to 0.8 release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jun 05 2011 Shakthi Kannan <shakthimaan [AT] fedoraproject DOT org> - 0.7-1
- Initial package.
