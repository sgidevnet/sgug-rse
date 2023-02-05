%define debug_package %{nil}

Summary: GnuPG integration scripts for Pine
Name:    ez-pine-gpg
Version: 0.4h
Release: 16%{?dist}
License: GPLv2+
URL:     http://business-php.com/opensource/ez-pine-gpg/

Source0: http://business-php.com/opensource/%{name}/%{name}_v%{version}.tgz

BuildArch: noarch

%description
ez-pine-gpg is a set of scripts that allows beginners and experts to use gpg
with Pine.

%prep
%setup -q -n %{name}

%build
echo "Nothing to build."

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
./install %{buildroot}%{_bindir}
for f in %{buildroot}%{_bindir}/ez-pine-gpg* ; do
    sed -i -e 's|%{buildroot}||g' ${f}
done

cat << EOF > pine-config
In pine, press: [M]ain [S]etup [C]onfigure
and add these filters:

display-filters =  _LEADING("-----BEGIN PGP")_ %{_bindir}/ez-pine-gpg-incoming
sending-filters =  %{_bindir}/ez-pine-gpg-sign-and-encrypt _INCLUDEALLHDRS_ _RECIPIENTS_
                   %{_bindir}/ez-pine-gpg-encrypt _RECIPIENTS_
                   %{_bindir}/ez-pine-gpg-sign _INCLUDEALLHDRS_

You may also install the ez-pine-gpg-symmetric sending filter.  See the
README for details.
EOF

%files
%doc README pine-config gpl.txt
%{_bindir}/ez-pine-gpg-encrypt
%{_bindir}/ez-pine-gpg-helper-recipient
%{_bindir}/ez-pine-gpg-helper-sender
%{_bindir}/ez-pine-gpg-incoming
%{_bindir}/ez-pine-gpg-sign
%{_bindir}/ez-pine-gpg-sign-and-encrypt
%{_bindir}/ez-pine-gpg-symmetric

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4h-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4h-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4h-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4h-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4h-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4h-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4h-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4h-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4h-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4h-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4h-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4h-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4h-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4h-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri May 21 2010 David Cantrell <dcantrell@redhat.com> - 0.4h-2
- Do not use RPM macros for basic commands in the spec file

* Tue May 18 2010 David Cantrell <dcantrell@redhat.com> - 0.4h-1
- Initial package (#549004)
