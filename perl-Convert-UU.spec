%define upstream_name    Convert-UU
%define upstream_version 0.5201

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	UUencode and UUdecode
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Convert/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
* * uuencode

  uuencode() takes as the first argument a string that is to be uuencoded.
  Note, that it is the string that is encoded, not a filename.
  Alternatively a filehandle may be passed that must be opened for reading.
  It returns the uuencoded string including 'begin' and 'end'. Second and
  third argument are optional and specify filename and mode. If unspecified
  these default to "uuencode.uu" and 644.

* * uudecode

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc ChangeLog README META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*
%{_bindir}/puudecode
%{_bindir}/puuencode
%{_mandir}/man1/puudecode.1*
%{_mandir}/man1/puuencode.1*



%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.520.100-4mdv2012.0
+ Revision: 765114
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.520.100-3
+ Revision: 763757
- bump release
- rebuilt for perl-5.14.x

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 0.5201

* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.520.100-2
+ Revision: 653559
- rebuild for updated spec-helper

  + Matthew Dawkins <mattydaw@mandriva.org>
    - replaced lzma extention with wildcard

* Tue Aug 31 2010 Jérôme Quelin <jquelin@mandriva.org> 0.520.100-1mdv2011.0
+ Revision: 574777
- import perl-Convert-UU

