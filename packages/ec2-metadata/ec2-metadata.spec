Name:           ec2-metadata
Version:        0.1.1
Release:        10%{?dist}
Summary:        EC2 instance metadata query tool 

# note web site says "Apache License 2.0", but code actually bears
# an MIT-style license.
License:        MIT
URL:            http://aws.amazon.com/code/1825
Source0:        http://s3.amazonaws.com/ec2metadata/ec2-metadata

Requires:       bash, curl

BuildArch:      noarch


%description
A simple bash script that uses curl to query the EC2 instance metadata from
within an instance running in Amazon EC2 or another cloud provider with a
compatible metadata service.
 
%prep
# none

%build
# none

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_bindir}
install -p -m 755 %{SOURCE0} $RPM_BUILD_ROOT/%{_bindir}/

%files
%defattr(755, root, root, -)
%{_bindir}/%{name}


%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 10 2013 Matthew Miller <mattdm@fedoraproject.org> 0.1.1-1
- use version number from file itself rather than date
- preserve timestamp

* Tue Nov 13 2012 Matthew Miller <mattdm@fedoraproject.org> 2012.08.30-2
- minor packaging tweaks: buildroot for EPEL5, license to MIT

* Tue Nov 13 2012 Matthew Miller <mattdm@fedoraproject.org> 2012.08.30-1
- initial package
